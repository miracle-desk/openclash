import requests
import yaml
import uuid
import os

def get_update_filter_proxies(urls):
    filtered_accounts = []
    sg_accounts = []
#    us_accounts = []
    relay_accounts = []
    premium_accounts = []
    used_uuids = set()  # Set untuk menyimpan UUID yang telah digunakan

    for url in urls:
        response = requests.get(url)
        data = response.text

        lines = data.split("\n")

        for line in lines:
            line = line.strip()
# variant1  if line.startswith("- ") and ("RELAY-" in line or "SG-" in line or "🇺🇸US-" in line) and "headers" in line and "Host" in line:
            if line.startswith("- ") and ("RELAY-" in line or "SG-" in line) and "headers" in line and "Host" in line:
                entry = yaml.safe_load(line[2:])
                uuid_ = entry.get("uuid")

                # Memeriksa apakah UUID sudah ada dalam set
                if uuid_ and uuid_ not in used_uuids:
                    filtered_accounts.append(line)
                    used_uuids.add(uuid_)  # Menambahkan UUID ke dalam set
                elif "RELAY-" in line and "headers" in line and "Host" in line:
                    relay_accounts.append(line)
                elif "SG-" in line and "headers" in line and "Host" in line:
                    sg_accounts.append(line)
#                elif "🇺🇸US-" in line and "headers" in line and "Host" in line:
#                    us_accounts.append(line)

    # Sort the account entries
    filtered_accounts.extend(sorted(relay_accounts)) 
    filtered_accounts.extend(sorted(sg_accounts))
#    filtered_accounts.extend(sorted(us_accounts))

    # Prepare the account entries with the desired structure
    formatted_accounts_1= []

    for account in filtered_accounts:
        entry = yaml.safe_load(account[2:])
        if "server" in entry:
            entry["server"] = "cvs-deo.shopeemobile.com"
        if "udp" not in entry:
            entry["udp"] = True
#        if "key" not in entry:
#            entry["key"] = "value"

        formatted_accounts_1.append(entry)
   
    formatted_accounts_2= []

    for account in filtered_accounts:
        entry = yaml.safe_load(account[2:])
        if "server" in entry:
            entry["server"] = "cvs-deo.shopeemobile.com"
        if "udp" not in entry:
            entry["udp"] = True
#        if "key" not in entry:
#            entry["key"] = "value"

        formatted_accounts_2.append(entry)

    # Prepare the YAML data
    yaml_data_1 = yaml.dump({"proxies": formatted_accounts_1}, sort_keys=False, allow_unicode=True)
    yaml_data_2 = yaml.dump({"proxies": formatted_accounts_2}, sort_keys=False, allow_unicode=True)

    # Write the filtered accounts to the YAML files with UTF-8 encoding
    output_dir_1 = "backup/proxy_provider"
    output_dir_2 = "backup/proxy_provider"
    output_path_1 = os.path.join(output_dir_1, "filter-liv.yaml")
    output_path_2 = os.path.join(output_dir_2, "filter-XL.yaml")

    # Create the folders if they don't exist
    os.makedirs(output_dir_1, exist_ok=True)
    os.makedirs(output_dir_2, exist_ok=True)

    with open(output_path_1, "w", encoding="utf-8") as file:
        file.write(yaml_data_1)

    with open(output_path_2, "w", encoding="utf-8") as file:
        file.write(yaml_data_2)

    total_accounts = len(filtered_accounts)
    sg_count = len(sg_accounts)
#    us_count = len(us_accounts)
    relay_count = len(relay_accounts)
    premium_count = len(premium_accounts)

    print(f"Total 'SG' accounts written: {sg_count}")
#    print(f"Total 'US' accounts written: {us_count}")
    print(f"Total 'RELAY' accounts written: {relay_count}")
    print(f"Total premium accounts: {premium_count}")
    print(f"Total accounts written: {total_accounts}")

    print("Files successfully created in the folders", output_dir_1, "and", output_dir_2)

urls = [
    'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml',
#    'https://mi-desk.neocities.org/clash/proxy_provider/SG_server_yml.txt'
]

get_update_filter_proxies(urls)
