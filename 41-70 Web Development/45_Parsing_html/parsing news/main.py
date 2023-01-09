from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
# print(yc_webpage)

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title.getText() + "\n")

article_tags = soup.select(selector=".titleline a")
article_texts = []
article_links = []

# skipping unwanted links
for tag in range(0, len(article_tags), 2):
    text = article_tags[tag].getText()
    article_texts.append(text)
    link = article_tags[tag].get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ = "score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_number = max(article_upvotes)
article_index = article_upvotes.index(max_number)
print(article_texts[article_index])
print(f"Link: {article_links[article_index]}")
print(f"Score: {max_number}")