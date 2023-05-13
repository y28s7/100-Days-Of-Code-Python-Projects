from bs4 import BeautifulSoup

with open("dummy-website.html", mode="r") as website:
    contents = website.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title, "\n")  # prints the line of html code with the title tag
print(soup.title.string, "\n")  # prints the content of the title tag

print(soup.prettify(), "\n")  # prints an indented version of the entire document

print(soup.a, "\n")  # prints the FIRST "a" tag it finds

all_anchor_tags = soup.find_all(name="a")  # finds all anchor tags (its a list with each item being each
# line containing the anchor tag
print(all_anchor_tags, "\n")

for tag in all_anchor_tags:
    print(tag.getText())  # prints the actual text of the anchor tag
    print(tag.get("href"), "\n")  # prints the href of the anchor tag

heading = soup.find(name="h1", id="name")  # gets the FIRST h1 with an id of "name"
print(heading, "\n")

class_heading = soup.find(class_="heading")  # gets the FIRST element with a class of "heading"
print(class_heading, "\n")

company_url = soup.select_one(selector="p a")  # a css selector can be inputted into the "selector" attribute and it
# will function the same way as selecting an element in css code. can also use # and . as you do in css. NOTE:
# soup.select_one() only finds the FIRST element, as with soup.find()
print(company_url, "\n")

headings = soup.select(selector=".heading")  # finds ALL html elements with a class of "heading"
print(headings, "\n")
