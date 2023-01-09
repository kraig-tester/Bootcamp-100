import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all(name="h3", class_="title")

contents = ""
for tag in movies[::-1]:
    contents += f"{tag.getText()}\n"

with open("movies.txt", mode="w", encoding="utf8") as file:
    file.write(contents)