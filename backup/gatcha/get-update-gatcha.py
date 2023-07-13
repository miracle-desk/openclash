import requests
import yaml
import uuid
import os

def get_update_filter_proxies(urls):
    filtered_accounts = []
    sg_accounts = []
    us_accounts = []
    relay_accounts = []
    premium_accounts = []

    for url in urls:
        response = requests.get(url)
        data = response.text

        lines = data.split("\n")

        for line in lines:
            line = line.strip()
            if line.startswith("- ") and ("RELAY-" in line or "SG-" in line or "🇺🇸US-" in line) and "headers" in line and "Host" in line:
                entry = yaml.safe_load(line[2:])
                if entry and "xmbb.net" in line:
                    filtered_accounts.insert(0, line)
                    premium_accounts.append(line)
                elif "meetzoom.disnet.gq" in line:
                    filtered_accounts.insert(1, line)
                    premium_accounts.append(line)
                elif "sg.wyhkaa0.tk" in line:
                    filtered_accounts.insert(2, line)
                    premium_accounts.append(line)
                elif "linkedin.disnet.gq" in line:
                    filtered_accounts.insert(3, line)
                    premium_accounts.append(line)
                elif "sshmax.xyz" in line:
                    filtered_accounts.insert(4, line)
                elif "mainssh.xyz" in line:
                    filtered_accounts.insert(5, line)
                elif "jp2.mlxg.org" in line:
                    filtered_accounts.insert(6, line)
                elif "ming2.kiwireich.com" in line:
                    filtered_accounts.insert(7, line)
                elif "2.lowh.net" in line:
                    filtered_accounts.insert(8, line)
                elif "v2ray1.udpgw.com" in line:
                    filtered_accounts.insert(9, line)
                elif "link2.kuaidog001.top" in line:
                    filtered_accounts.insert(10, line)
                elif "sg1b.obfs.xyz" in line:
                    filtered_accounts.insert(11, line)
                elif "sg2-mlb.securev2ray.com" in line:
                    filtered_accounts.insert(12, line)
                elif "hk.kkpp.online" in line:
                    filtered_accounts.insert(13, line)
                elif "rochinet.fullaccesstointernet.cn.eu.org" in line:
                    filtered_accounts.insert(14, line)
                elif "1.freek1.xyz" in line:
                    filtered_accounts.insert(15, line)
                elif "vceu.vpn66.eu.org" in line:
                    filtered_accounts.insert(16, line)
                elif "rusabdfs.76898102.xyz" in line:
                    filtered_accounts.insert(17, line)
                elif "mp.microsoft.com" in line:
                    filtered_accounts.insert(18, line)
                elif "trojan.bonds.id" in line:
                    filtered_accounts.insert(19, line)
                elif ".test3.net" in line:
                    filtered_accounts.insert(20, line)
                elif "gorgorchicken.one" in line:
                    filtered_accounts.insert(21, line)
                elif "ssrsub.com" in line:
                    filtered_accounts.insert(22, line)
                elif "114514782.xyz" in line:
                    filtered_accounts.insert(23, line)
                elif ".zuhyp4107.workers.dev" in line:
                    filtered_accounts.insert(24, line)
                elif ".992688.xyz" in line:
                    filtered_accounts.insert(25, line)
                elif "starsea.vip" in line:
                    filtered_accounts.insert(26, line)
                elif "dedi2.1808.cf" in line:
                    filtered_accounts.insert(27, line)
                elif "amstd.digires.shop" in line:
                    filtered_accounts.insert(28, line)
                elif "jpnat1.doinb.tk" in line:
                    filtered_accounts.insert(29, line)
                elif ".workers.dev" in line:
                    filtered_accounts.insert(30, line)
                elif ".polycdn.com" in line:
                    filtered_accounts.insert(31, line)
                elif ".encrypted.my.id" in line:
                    filtered_accounts.insert(32, line)
                elif "RELAY-" in line and "headers" in line and "Host" in line:
                    relay_accounts.append(line)
                elif "SG-" in line and "headers" in line and "Host" in line:
                    sg_accounts.append(line)
                elif "🇺🇸US-" in line and "headers" in line and "Host" in line:
                    us_accounts.append(line)

    # Sort the account entries
    filtered_accounts.extend(sorted(relay_accounts)) 
    filtered_accounts.extend(sorted(sg_accounts))
    filtered_accounts.extend(sorted(us_accounts))

    # Prepare the account entries with the desired structure
    formatted_accounts_1= []

    for account in filtered_accounts:
        entry = yaml.safe_load(account[2:])
        if "server" in entry:
            entry["server"] = "104.21.8.121"
        if "xudp" not in entry:
            entry["xudp"] = True
        if "key" not in entry:
            entry["key"] = "value"

        formatted_accounts_1.append(entry)
   
    formatted_accounts_2= []

    for account in filtered_accounts:
        entry = yaml.safe_load(account[2:])
        if "server" in entry:
            entry["server"] = "104.17.3.81"
        if "xudp" not in entry:
            entry["xudp"] = True
        if "key" not in entry:
            entry["key"] = "value"

        formatted_accounts_2.append(entry)

    # Prepare the YAML data
    yaml_data_1 = yaml.dump({"proxies": formatted_accounts_1}, sort_keys=False, allow_unicode=True)
    yaml_data_2 = yaml.dump({"proxies": formatted_accounts_2}, sort_keys=False, allow_unicode=True)

    # Write the filtered accounts to the YAML files with UTF-8 encoding
    output_dir_1 = "backup/proxy_provider"
    output_dir_2 = "backup/proxy_provider"
    output_path_1 = os.path.join(output_dir_1, "filter-liv.yaml")
    output_path_2 = os.path.join(output_dir_2, "filter-akrab.yaml")

    # Create the folders if they don't exist
    os.makedirs(output_dir_1, exist_ok=True)
    os.makedirs(output_dir_2, exist_ok=True)

    with open(output_path_1, "w", encoding="utf-8") as file:
        file.write(yaml_data_1)

    with open(output_path_2, "w", encoding="utf-8") as file:
        file.write(yaml_data_2)

    total_accounts = len(filtered_accounts)
    sg_count = len(sg_accounts)
    us_count = len(us_accounts)
    relay_count = len(relay_accounts)
    premium_count = len(premium_accounts)

    print(f"Total 'SG' accounts written: {sg_count}")
    print(f"Total 'US' accounts written: {us_count}")
    print(f"Total 'RELAY' accounts written: {relay_count}")
    print(f"Total premium accounts: {premium_count}")
    print(f"Total accounts written: {total_accounts}")

    print("Files successfully created in the folders", output_dir_1, "and", output_dir_2)

urls = [
    'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml',
    'https://mi-desk.neocities.org/clash/proxy_provider/SG_server_yml.txt'
]

get_update_filter_proxies(urls)

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
    def fool_custom_sort_key(acc):
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
    accounts.sort(key=fool_custom_sort_key)

    # Menentukan path file YAML
    output_dir = "backup/proxy_provider"
    output_path = os.path.join(output_dir, "fool-provider.yaml")

    # Membuat folder jika belum ada
    os.makedirs(output_dir, exist_ok=True)

    # Membuat file YAML baru
    with open(output_path, "w") as file:
        # Menulis data akun terhubung ke dalam file YAML
        yaml.dump({"proxies": accounts}, file, sort_keys=False)

    print("File fool-provider.yaml berhasil dibuat di folder", output_dir)

get_update_fool_proxies("https://fool.azurewebsites.net/get?format=clash&mode=cdn&cdn=104.17.3.81&network=ws&arg=xudp,key:value&vpn=trojan,vmess,vless&region=Asia&cc=SG,ID,JP&exclude=amazon&limit=3&pass=1oqrsj6c")
