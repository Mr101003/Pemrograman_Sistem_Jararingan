import requests
from bs4 import BeautifulSoup

url = input('masukkan URL : ')
resp = requests.get(url)
page = resp.text
 
bs = BeautifulSoup(page, "html.parser")
# scrap title
title = bs.title
print(title)

links = bs.find_all('a')

for tag_a in links:
    print(f"{tag_a.text} -> {tag_a['href']}")
# print(resp.text)