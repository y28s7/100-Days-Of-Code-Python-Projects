from bs4 import BeautifulSoup
import requests

html_code = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(html_code, "html.parser")

articles = soup.select(selector="span.titleline > a")
article_links = []
article_texts = []
for article in articles:
    link = article.get("href")
    text = article.getText()

    article_links.append(link)
    article_texts.append(text)

article_upvotes = [int(score.getText().split()[0]) for score in soup.select(selector="span.score")]

print(
    f"article-texts: {article_texts}\n"
    f"article-links: {article_links}\n"
    f"article-upvote: {article_upvotes}\n"
)

highest_upvote = article_upvotes.index(max(article_upvotes))

print(
    f"highest-upvote-text: {article_texts[highest_upvote]}\n"
    f"highest-upvote-link: {article_links[highest_upvote]}\n"
    f"highest-upvote-count: {article_upvotes[highest_upvote]}\n"
)
