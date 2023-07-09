import requests
import yaml
import subprocess

def get_ping(account):
    server = account.get("server")
    ping_result = subprocess.run(["ping", "-n", "4", server], capture_output=True, text=True)
    lines = ping_result.stdout.strip().split("\n")
    last_line = lines[-1]
    if "time=" in last_line:
        ping_time = float(last_line.split("time=")[1].split("ms")[0])
        return ping_time
    else:
        return float("inf")

def get_proxies_with_lowest_ping(url, num_proxies):
    response = requests.get(url)
    data = response.text

    accounts = yaml.safe_load(data)
    filtered_accounts = [account for account in accounts.get("proxies", []) if account.get("server") and account.get("ws-opts") and account["ws-opts"].get("headers") and "Host" in account["ws-opts"]["headers"]]
    sorted_accounts = sorted(filtered_accounts, key=lambda x: get_ping(x))
    selected_accounts = sorted_accounts[:num_proxies]

    return selected_accounts

def main():
    url = "https://raw.githubusercontent.com/miracle-desk/Openclash/main/Backup/proxy_provider/filter-proxies.yaml"
    file_path = "filterPing.yaml"
    num_proxies = 40

    # Get the proxies with the lowest ping
    selected_accounts = get_proxies_with_lowest_ping(url, num_proxies)

    # Write the selected accounts to the YAML file
    with open(file_path, "w", encoding="utf-8") as file:
        yaml.dump({"proxies": selected_accounts}, file, sort_keys=False)

    print("Akun berhasil ditulis ke file filterPing.yaml")
    print(f"Total akun yang terbaca: {len(selected_accounts)}")

if __name__ == "__main__":
    main()
