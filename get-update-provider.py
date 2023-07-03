import requests
import yaml

accounts = []  # List untuk menyimpan akun yang telah dikumpulkan

# Perulangan untuk membuka URL sebanyak 10 kali
for _ in range(10):
    url = "https://fool.azurewebsites.net/get?format=clash&mode=cdn&cdn=104.17.3.81&network=ws&arg=xudp,key:value&vpn=trojan,vmess,vless&region=Asia&cc=SG,ID,JP&exclude=amazon&limit=3&pass=1oqrsj6c"  # Ganti dengan URL yang sesuai
    
    response = requests.get(url)
    data = response.text
    
    # Parsing akun dari teks menggunakan library YAML
    parsed_data = yaml.safe_load(data)
    
    # Memeriksa dan menambahkan akun ke dalam list jika host dan port belum ada
    for account in parsed_data["proxies"]:
        host = account["servername"]
        port = account["port"]
        
        # Memeriksa apakah host dan port sudah ada dalam list akun
        if (host, port) not in [(acc["servername"], acc["port"]) for acc in accounts]:
            accounts.append(account)

# Menentukan kunci khusus untuk mengurutkan proxies berdasarkan nama proxies dengan aturan yang diberikan, karena di clash saya mau menggunakan mode fallback
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

# Membuat file YAML baru
with open("fool-provider.yaml", "w") as file:
    # Menulis data akun ke dalam file YAML
    yaml.dump({"proxies": accounts}, file, sort_keys=False)  # Menggunakan sort_keys=False agar urutan penulisan tetap

print("File fool-provider.yaml berhasil dibuat.")