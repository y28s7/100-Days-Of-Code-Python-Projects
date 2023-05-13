import requests
import smtplib
import random
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\email-stuff.env")
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\stock-news-notifier.env")

STOCK = "AMZN"
COMPANY_NAME = "Amazon.com, Inc"

alphavantage_api_key = os.environ["ALPHAVANTAGE_API_KEY"]

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": alphavantage_api_key,
}

alphavantage_response = requests.get(url="https://www.alphavantage.co/query?", params=alphavantage_parameters)
alphavantage_response.raise_for_status()

total_data = alphavantage_response.json()["Time Series (Daily)"]
daily_close_data = [value["4. close"] for (key, value) in total_data.items()]

# "lbd" stands for "last business day"
lbd_close = float(daily_close_data[0])
day_before_lbd_close = float(daily_close_data[1])

price_difference = ((lbd_close / day_before_lbd_close) - 1) * 100
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

if abs(price_difference) > 5:
    newsapi_parameters = {
        "q": COMPANY_NAME,
        "apiKey": os.environ["NEWS_API_KEY"]
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=newsapi_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()["articles"]
    articles = [news_data[i] for i in range(0, 3)]
    article1message = f"Headline: {articles[0]['title']}\nBrief: {articles[0]['description']}\nURL: " \
                      f"{articles[0]['url']}\n" \
                      f"Article Published at {articles[0]['publishedAt'].split('T')[0]}"

    article2message = f"Headline: {articles[1]['title']}\nBrief: {articles[1]['description']}\nURL: " \
                      f"{articles[1]['url']}\n" \
                      f"Article Published at {articles[1]['publishedAt'].split('T')[0]}"

    article3message = f"Headline: {articles[2]['title']}\nBrief: {articles[2]['description']}\nURL: " \
                      f"{articles[2]['url']}\n" \
                      f"Article Published at {articles[2]['publishedAt'].split('T')[0]}"

    articles_to_display1 = [article1message, article2message, article3message]

    if price_difference < 0:
        difference_display = f"Down {round(abs(price_difference), 2)}%"
    else:
        difference_display = f"Up {round(abs(price_difference), 2)}%"

    articles_to_display = []

    for text in articles_to_display1:
        text = f"{STOCK}: {difference_display}\n" + text
        articles_to_display.append(text)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

    email = os.environ.get("EMAIL")
    password = os.environ.get("EMAIL_APP_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: {STOCK}: {difference_display}\n\n"
                                                                 f"{random.choice(articles_to_display)}")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market """
