import requests
import yaml
import os

def get_update_filter_proxies(urls):
    sg_accounts = {}
    relay_accounts = {}

    for url in urls:
        response = requests.get(url)
        data = response.text

        lines = data.split("\n")

        for line in lines:
            line = line.strip()
            if line.startswith("- ") and ("RELAY-" in line or "SG-" in line) and "headers" in line and "Host" in line:
                entry = yaml.safe_load(line[2:])
                uuid_ = entry.get("uuid")

                # Memeriksa apakah UUID sudah ada dalam set
                if uuid_:
                    if "RELAY-" in line:
                        if uuid_ not in relay_accounts:
                            relay_accounts[uuid_] = entry
                    elif "SG-" in line:
                        if uuid_ not in sg_accounts:
                            sg_accounts[uuid_] = entry

    # Modifikasi entri akun sebelum menulisnya ke file YAML
    for accounts in [sg_accounts, relay_accounts]:
        for uuid_, entry in accounts.items():
            if "server" in entry:
                entry["server"] = "cvs-deo.shopeemobile.com"
            if "udp" not in entry:
                entry["udp"] = True
            # Masukkan logika tambahan di sini, jika diperlukan

    # Prepare the YAML data
    formatted_accounts = list(sg_accounts.values()) + list(relay_accounts.values())

    # Write the filtered accounts to the YAML file with UTF-8 encoding
    output_dir = "backup/proxy_provider"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "filtered-account.yaml")
    with open(output_path, "w", encoding="utf-8") as file:
        yaml.dump({"proxies": formatted_accounts}, file, sort_keys=False, allow_unicode=True)

    total_sg_accounts = len(sg_accounts)
    total_relay_accounts = len(relay_accounts)
    
    total_accounts = total_sg_accounts + total_relay_accounts

    print(f"Total 'SG' accounts written: {total_sg_accounts}")
    print(f"Total 'RELAY' accounts written: {total_relay_accounts}")
    print(f"Total accounts written: {total_accounts}")
    print("File successfully created:", output_path)

urls = [
    'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml',
]

get_update_filter_proxies(urls)
