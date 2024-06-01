import requests
from bs4 import BeautifulSoup

url = "https://library.nurulfikri.ac.id/index.php?p=show_detail&id=3219"
resp = requests.get(url)
page = resp.text

bs = BeautifulSoup(page, "html.parser")
# Extract title
print(bs.h4.text)
