# Web Scraping using BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

# Step 3: HTML tree traversal (Targeting Data)
# Getting the title
title = soup.title
print(title)

# Getting all the paragraphs
paras = soup.find_all('p')
print(paras)

# Getting first element of HTML page
print(soup.find('p'))

# Getting classes of any element of HTML page
print(soup.find('p')['class'])

# Find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# Get the text from tag/soup 
print(soup.find('p').get_text())
# print(soup.get_text())

# Getting all the anchors
anchors = soup.find_all('a')
print(anchors)

# Get all the links on the page
all_links = set()
for link in anchors:
    if link.get('href') != '#':
        all_links.add("https://codewithharry" + link.get('href'))

print(all_links)

# Comments:
markup = "<p><!-- This is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)

# Children, parent, next_sibling and previous_siblings:
# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent)
for elem in navbarSupportedContent.contents:
    print(elem)

for item in navbarSupportedContent.strings:
    print(item)

print(navbarSupportedContent.parent)
for item in navbarSupportedContent.parents:
    print(item.name)

print(navbarSupportedContent.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('#loginModal')
print(elem)

elem = soup.select('.modal-footer')
print(elem)
