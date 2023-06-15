# adblock
trial automatic update rule adblock openclash

Untuk menggunakan, edit `config.yaml` pada `/etc/openclash/config/config.yaml` seperti ini:
```
rule-providers:
  rule_oisd-full:
    type: http
    behavior: classical
    path: "./rule_provider/rule_oisd-full.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/my_adblock_list/main/rule_oisd-full.yaml
    interval: 86400 # Update rules every 24 hours
    
rules:
- RULE-SET,Direct,DIRECT
- RULE-SET,XL_Akrab,DIRECT
- RULE-SET,Reject,REJECT
- RULE-SET,rule_personalads,REJECT
- RULE-SET,rule_basicads,REJECT
- RULE-SET,rule_privacy,REJECT
- RULE-SET,rule_malicious,REJECT
- RULE-SET,rule_maliciousip,REJECT
- RULE-SET,rule_adguard-dns,REJECT
- RULE-SET,rule_abpindo,REJECT
- RULE-SET,rule_adaway,REJECT
- RULE-SET,rule_hijacking,REJECT
#
#==================CUSTOM=======================
- RULE-SET,rule_adult,REJECT
- RULE-SET,rule_nsfw,REJECT
#==================CUSTOM=======================
#
#- RULE-SET,rule_umum,GLOBAL
- RULE-SET,rule_speedtest,GLOBAL
- MATCH,GLOBAL
```
