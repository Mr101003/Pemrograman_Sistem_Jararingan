import requests
from bs4 import BeautifulSoup

url = 'https://elena.nurulfikri.ac.id'
resp = requests.get(url)
page = resp.text

bs = BeautifulSoup(page, "html.parser")
# Extract title
title = bs.title
# print(title)
print(title.text)

links = bs.find_all('a')

for tag_a in links:
    print(f"{tag_a.text} -> {tag_a['href']}")
