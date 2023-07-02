import requests
import yaml

accounts = []  # List untuk menyimpan akun yang telah dikumpulkan

# Perulangan untuk membuka URL sebanyak 10 kali
for _ in range(10):
    url = "https://fool.azurewebsites.net/get?format=clash&mode=cdn&cdn=104.17.3.81&tls=1&network=ws&port=443&arg=xudp,key:value&vpn=trojan,vmess,vless&region=Asia&cc=SG,ID&limit=3&pass=1oqrsj6c"  # Ganti dengan URL yang sesuai
    
    response = requests.get(url)
    data = response.text
    
    # Parsing akun dari teks menggunakan library YAML
    parsed_data = yaml.safe_load(data)
    
    # Memeriksa dan menambahkan akun ke dalam list jika host belum ada
    for account in parsed_data["proxies"]:
        host = account["servername"]
        
        # Memeriksa apakah host sudah ada dalam list akun
        if host not in [acc["servername"] for acc in accounts]:
            accounts.append(account)

# Membuat file YAML baru
with open("fool-provider.yaml", "w") as file:
    # Menulis data akun ke dalam file YAML
    yaml.dump({"proxies": accounts}, file)

print("File fool-provider.yaml berhasil dibuat.")