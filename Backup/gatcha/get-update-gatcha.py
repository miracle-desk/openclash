import requests
import yaml
import uuid
import os

def get_update_filter_proxies(url):
    response = requests.get(url)
    data = response.text

    filtered_accounts = []
    sg_accounts = []
    relay_accounts = []

    lines = data.split("\n")

    for line in lines:
        line = line.strip()
        if line.startswith("- ") and "RELAY" in line and "headers" in line:
            relay_accounts.append(line)
        elif line.startswith("- ") and "🇸🇬SG" in line and "headers" in line:
            sg_accounts.append(line)

    # Sort the account entries
    filtered_accounts.extend(sorted(sg_accounts))
    filtered_accounts.extend(sorted(relay_accounts))

    # Prepare the account entries with the desired structure
    formatted_accounts = []

    for account in filtered_accounts:
        entry = yaml.safe_load(account[2:])
        if "server" in entry:
            entry["server"] = "104.17.3.81"
        if "xudp" not in entry:
            entry["xudp"] = True
        if "key" not in entry:
            entry["key"] = "value"

        formatted_accounts.append(entry)

    # Prepare the YAML data
    yaml_data = yaml.dump({"proxies": formatted_accounts}, sort_keys=False, allow_unicode=True)

    # Write the filtered accounts to the YAML file with UTF-8 encoding
    output_dir = "Backup/proxy_provider"
    output_path = os.path.join(output_dir, "filter-proxies.yaml")
    
    # Membuat folder jika belum ada
    os.makedirs(output_dir, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(yaml_data)

    total_accounts = len(filtered_accounts)
    sg_count = len(sg_accounts)
    relay_count = len(relay_accounts)

    print(f"Total 'SG' accounts written: {sg_count}")
    print(f"Total 'RELAY' accounts written: {relay_count}")
    print(f"Total accounts written to filter-proxies.yaml: {total_accounts}")

    print("File filter-proxies.yaml berhasil dibuat di folder", output_dir)
def get_update_fool_proxies(url):
    accounts = []  # List untuk menyimpan akun yang telah dikumpulkan

    received_accounts = []  # List untuk menyimpan akun yang diterima sebelum parsing
    parsed_accounts = []  # List untuk menyimpan akun yang telah diparsing

    # Perulangan untuk membuka URL sebanyak 5 kali
    for _ in range(5):
        response = requests.get(url)
        data = response.text

        # Parsing akun dari teks menggunakan library YAML
        parsed_data = yaml.safe_load(data)

        # Memeriksa dan menambahkan akun ke dalam list jika uuid belum ada
        for account in parsed_data["proxies"]:
            uuid = account["uuid"]
            name = account["name"]
            server = account["server"]

            # Menyimpan akun yang diterima sebelum parsing
            received_accounts.append(account)
            print(f"received account: {name}")

            # Memeriksa apakah uuid sudah ada dalam list akun
            if uuid not in [acc["uuid"] for acc in accounts]:
                accounts.append(account)
                # Menyimpan akun yang telah diparsing
                parsed_accounts.append(account)
                print(f"parsed account: {name}")

    # Menghitung jumlah total akun yang diterima dan setelah parsing
    total_received = len(received_accounts)
    total_parsed = len(parsed_accounts)

    print(f"Total accounts received: {total_received}")
    print(f"Total accounts after parsed: {total_parsed}")

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

get_update_filter_proxies("https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml")
get_update_fool_proxies("https://fool.azurewebsites.net/get?format=clash&mode=cdn&cdn=104.17.3.81&network=ws&arg=xudp,key:value&vpn=trojan,vmess,vless&region=Asia&cc=SG,ID,JP&exclude=amazon&limit=3&pass=1oqrsj6c")
