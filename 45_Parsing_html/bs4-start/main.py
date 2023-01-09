from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

# print(contents)

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

print(soup.p)

all_p_tags = soup.find_all(name="p")
all_a_tags = soup.find_all(name="a")

for tag in all_a_tags:
    # bs4 tag class
    # print(type(tag)) 
    print(tag.name)
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

# selector works like css, used to choose first element that matches
company_url = soup.select_one(selector="p a")
name = soup.select_one(selector="#name")

print(company_url)
print(name)

# creates list with matching elements
headings = soup.select(".heading")
print(headings)

