import requests
import uuid
import yaml
import os
from ping3 import ping, verbose_ping

accounts = []  # List untuk menyimpan akun yang telah dikumpulkan

# Perulangan untuk membuka URL sebanyak 5 kali
for _ in range(5):
    url = "https://fool.azurewebsites.net/get?format=clash&mode=cdn&cdn=104.17.3.81&network=ws&arg=xudp,key:value&vpn=trojan,vmess,vless&region=Asia&cc=SG,ID,JP&exclude=amazon&limit=3&pass=1oqrsj6c"  # Ganti dengan URL yang sesuai

    # Parsing akun dari teks menggunakan library YAML
    response = requests.get(url)
    data = response.text
    parsed_data = yaml.safe_load(data)

    # Memeriksa koneksi internet dari setiap akun dan menambahkan ke dalam list jika terhubung
    for account in parsed_data["proxies"]:
        name = account["name"]
        server = account["server"]

        # Memeriksa koneksi internet dengan ping
        if ping(server, timeout=2) is not None:
            accounts.append(account)
            print(f"Akun {name} terhubung ke internet")
        else:
            print(f"Akun {name} tidak terhubung ke internet")

# Menentukan kunci khusus untuk mengurutkan proxies berdasarkan nama proxies dengan aturan yang diberikan
def custom_sort_key(acc):
    name = acc["name"]

    if "ORACLE" in name:
        return 1
    elif "CONTABO" in name:
        return 2
    elif "OCEAN" in name:
        return 3
    elif "AKAMAI" in name:
        return 4
    elif "DATACAMP" in name:
        return 5
    elif "MELBI" in name:
        return 6
    else:
        return 7  # Proxies yang tidak sesuai dengan aturan akan ditempatkan di akhir

# Mengurutkan proxies berdasarkan kunci khusus
accounts.sort(key=custom_sort_key)

# Menentukan path file YAML
output_dir = "Backup/proxy_provider"
output_path = os.path.join(output_dir, "fool-provider.yaml")

# Membuat folder jika belum ada
os.makedirs(output_dir, exist_ok=True)

# Membuat file YAML baru
with open(output_path, "w") as file:
    # Menulis data akun terhubung ke dalam file YAML
    yaml.dump({"proxies": accounts}, file, sort_keys=False)

print("File fool-provider.yaml berhasil dibuat di folder", output_dir)
