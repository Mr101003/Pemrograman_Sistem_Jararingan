import os
import re

# Fungsi untuk menjalankan perintah ping dan mengambil outputnya
def run_ping(address):
    try:
        # Menjalankan perintah ping dan menangkap outputnya
        ping_output = os.popen(f"ping -c 5 {address}").read()
        return ping_output
    except Exception as e:
        print(f"Error occurred while pinging {address}: {str(e)}")
        return None

# Fungsi untuk mengambil nilai rata-rata dari hasil ping pada baris terakhir
def get_last_ping_average(filename):
    try:
        with open(filename, 'r') as file:
            # Membaca baris terakhir dari file
            last_address = file.readlines()[-1].strip()
        # Menjalankan perintah ping untuk alamat terakhir
        ping_output = run_ping(last_address)
        if ping_output:
            # Menggunakan regular expression untuk mencocokkan waktu respons dari output ping
            pattern = r"time=(\d+\.\d+) ms"
            matches = re.findall(pattern, ping_output)
            
            # Mengkonversi nilai waktu respons menjadi float dan menghitung rata-ratanya
            if matches:
                times = [float(match) for match in matches]
                average = sum(times) / len(times)
                return average
            else:
                return None
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return None

# Baca alamat ping dari file teks
filename = "ping task/host_data.txt"

# Mengambil nilai rata-rata dari hasil ping pada baris terakhir
ping_average = get_last_ping_average(filename)

if ping_average is not None:
    print(f"Average ping time for the last address: {ping_average} ms")
else:
    print("No valid ping times found for the last address.")
