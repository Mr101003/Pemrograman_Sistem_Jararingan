import os

# Jalankan perintah 'ps aux' dan tangkap outputnya
result = os.popen('ps aux').read()

# Simpan output ke dalam file 'hasil_ps.txt'
with open('hasil_ps.txt', 'w') as f:
    f.write(result)

print("Hasil perintah 'ps aux' telah disimpan dalam file 'hasil_ps.txt'.")
