import requests
import sys
####LENGKAPI

from  math import ceil
if len(sys.argv) < 2:
	print("Gagal: pola untuk pencarian tidak ada")
	sys.exit()
 
keyword = sys.argv[1] ####LENGKAPI

url = f"https://library.nurulfikri.ac.id/index.php?JSONLD=true&keywords={keyword}&search=search"
resp = requests.get(url,"json")
try:
	data = resp.json()
	total_rows = data["total_rows"]
except:
	print("Tidak ada data yang ditemukan")
sys.exit() ####LENGKAPI

pages = ceil(int(total_rows)/int(data["records_each_page"]))
page = data["page"]
no = 1
web = "https://library.nurulfikri.ac.id"
books = []
while page <= pages: ####LENGKAPI:
	if page > 1:
		url = f"https://library.nurulfikri.ac.id/index.php?JSONLD=true&keywords={keyword}&search=search&page={page}"
		resp = requests.get(url) ####LENGKAPI
		data = resp.json()
	for item in data["@graph"]:
		books.append(item) ####LENGKAPI 
	page = page + 1
 
print()
print( f"Daftar pencarian buku dengan keyword '{keyword}' pada {web}" )
print( f"Ditemukan {total_rows} item" )

no = 1

for book in books : ####LENGKAPI
	names = []
	try:
		for name in book['author']['name']:
			nm = name.split(",")
			nm.reverse()
			names.append(" ".join(nm))
		author = ",".join(names)
	except:
		author = ""
		
	print()
	print(f"#{no}")
	print(f"Judul	: {book['name']}") ####LENGKAPI
	print(f"Penulis	: {author}")
	print(f"ISBN	: {book.get('isbn', 'tidak ada ISBN')}") ####LENGKAPI
	print(f"Penerbit: {book['publisher']}")
no+=1 ####LENGKAPI