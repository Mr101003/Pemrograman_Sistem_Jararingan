import requests
url = "http://192.168.200.64:8900/presensi"

data = {"nim":"0110222178", "nama":"Mu'adz"}

req = requests.post(url,data)
if req.status_code == 200:
    print(req.text)
else:
    print("presenssi gagal")
    print(req.text)