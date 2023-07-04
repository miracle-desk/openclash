import uuid
import requests
import yaml
import os

accounts = []  # List untuk menyimpan akun yang telah dikumpulkan

# Perulangan untuk membuka URL sebanyak 5 kali
for _ in range(5):
    url = "https://fool.azurewebsites.net/get?format=clash&mode=cdn&cdn=104.17.3.81&network=ws&arg=xudp,key:value&vpn=trojan,vmess,vless&region=Asia&cc=SG,ID,JP&exclude=amazon&limit=3&pass=1oqrsj6c"  # Ganti dengan URL yang sesuai
    
    response = requests.get(url)
    data = response.text
    
    # Parsing akun dari teks menggunakan library YAML
    parsed_data = yaml.safe_load(data)
    
    # Memeriksa dan menambahkan akun ke dalam list jika uuid belum ada
    for account in parsed_data["proxies"]:
        uuid = account["uuid"]
        
        # Memeriksa apakah uuid sudah ada dalam list akun
        if (uuid) not in [(acc["uuid"]) for acc in accounts]:
            accounts.append(account)

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
    elif "MELBI" in name:
        return 5
    else:
        return 6  # Proxies yang tidak sesuai dengan aturan akan ditempatkan di akhir

# Mengurutkan proxies berdasarkan kunci khusus
accounts.sort(key=custom_sort_key)

# Menentukan path file YAML
output_dir = "Backup/proxy_provider"
output_path = os.path.join(output_dir, "fool-provider.yaml")

# Membuat folder jika belum ada
os.makedirs(output_dir, exist_ok=True)

# Membuat file YAML baru
with open(output_path, "w") as file:
    # Menulis data akun ke dalam file YAML
    yaml.dump({"proxies": accounts}, file, sort_keys=False)

print("File fool-provider.yaml berhasil dibuat di folder", output_dir)
