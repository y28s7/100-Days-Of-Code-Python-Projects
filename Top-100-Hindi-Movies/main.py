from bs4 import BeautifulSoup
import requests
import unicodedata

html_code = requests.get(url="https://www.timeout.com/film/the-100-best-bollywood-movies-the-list").text
soup = BeautifulSoup(html_code, "html.parser")

movies_raw = soup.select(selector="h3._h3_cuogz_1")
movies = [unicodedata.normalize("NFKD", heading.getText()) for heading in movies_raw]
movies.reverse()

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        if movie == len(movies):
            file.write(f"{movie}")
        else:
            file.write(f"{movie}\n")
