# Openclash Rule Set
backup file openclash
rule-providers:
#
# ================= RULE SET DIRECT==================
#
  Direct:
    type: file
    behavior: classical
    path: "./rule_provider/direct.yaml"
  XL_Akrab:
    type: http
    behavior: classical
    path: "./rule_provider/XL_Akrab.yaml"
    url: https://raw.githubusercontent.com/helmiau/clashrules/main/rule_provider/XL_Akrab.yaml
    interval: 14400
#
# ============== RULE SET MATCH GLOBAL ==============
#
  rule_umum:
    type: http
    behavior: classical
    path: "./rule_provider/rule_umum.yaml"
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_umum.yaml
    interval: 86400
  rule_speedtest:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_speedtest.yaml
    path: "./rule_provider/rule_speedtest.yaml"
    interval: 86400
#
# ================= RULE SET REJECT =================
#
  Reject:
    type: file
    behavior: classical
    path: "./rule_provider/reject.yaml"
  rule_personalads:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_personalads.yaml
    path: "./rule_provider/rule_personalads.yaml"
    interval: 86400
  rule_basicads:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_basicads.yaml
    path: "./rule_provider/rule_basicads.yaml"
    interval: 43200
  rule_privacy:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_privacy.yaml
    path: "./rule_provider/rule_privacy.yaml"
    interval: 86400
  rule_malicious:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_malicious.yaml
    path: "./rule_provider/rule_malicious.yaml"
    interval: 43200
  rule_maliciousip:
    type: http
    behavior: ipcidr
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_maliciousip.yaml
    path: "./rule_provider/rule_maliciousip.yaml"
    interval: 43200
  rule_adguard-dns:
    type: http
    behavior: classical
    path: "./rule_provider/AdguardDNS.yaml"
    url: https://raw.githubusercontent.com/hillz2/openclash_adblock/main/AdguardDNS.yaml
    interval: 14400 # Update rules every 4 hours
  rule_abpindo:
    type: http
    behavior: classical
    path: "./rule_provider/ABPindo.yaml"
    url: https://raw.githubusercontent.com/hillz2/openclash_adblock/main/ABPindo.yaml
    interval: 14400 # Update rules every 4 hours
  rule_hijacking:
    type: http
    behavior: classical
    path: "./rule_provider/rule_hijacking.yaml"
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_hijacking.yaml
    interval: 86400
  rule_adult:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_porn.yaml
    path: "./rule_provider/rule_porn.yaml"
    interval: 86400
  rule_nsfw:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_nsfw.yaml
    path: "./rule_provider/rule_nsfw.yaml"
    interval: 43200
  rule_adaway:
    type: http
    behavior: classical
    path: "./rule_provider/adaway.yaml"
    url: https://raw.githubusercontent.com/hillz2/openclash_adblock/main/adaway.yaml
    interval: 14400
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
