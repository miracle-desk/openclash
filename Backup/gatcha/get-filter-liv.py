import os
import requests
import yaml

def main():
    # URL file YAML akun clash
    url = "https://raw.githubusercontent.com/miracle-desk/Openclash/main/Backup/proxy_provider/filter-proxies.yaml"

    # Membuat direktori Backup/proxy_provider jika belum ada
    os.makedirs("Backup/proxy_provider", exist_ok=True)

    # Mengambil konten file YAML dari URL
    response = requests.get(url)
    data = response.text

    # Parsing file YAML
    accounts = yaml.safe_load(data)
    filtered_accounts = []

    # Filter akun dan ubah server menjadi 104.21.8.121
    for account in accounts.get("proxies", []):
        if account.get("ws-opts") and account["ws-opts"].get("headers") and "Host" in account["ws-opts"]["headers"]:
            account["server"] = "104.21.8.121"
            filtered_accounts.append(account)

    # Batasi jumlah akun yang diambil menjadi 40
    filtered_accounts = filtered_accounts[:40]

    # Menulis hasil filter ke file YAML
    file_path = "Backup/proxy_provider/filter-liv.yaml"
    with open(file_path, "w", encoding="utf-8") as file:
        yaml.dump({"proxies": filtered_accounts}, file, sort_keys=False)

    total_filtered_accounts = len(filtered_accounts)
    total_accounts = len(accounts.get("proxies", []))

    print("Akun berhasil ditulis ke file filter-liv.yaml")
    print(f"Total akun yang diambil: {total_filtered_accounts}")
    print(f"Total akun yang terdeteksi: {total_accounts}")

if __name__ == "__main__":
    main()
