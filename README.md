# config.yaml
```yaml
---
rule-providers:
# ================= RULE SET DIRECT==================
  Direct:
    type: file
    behavior: classical
    path: "./rule_provider/direct.yaml"
  xl-akrab:
    type: http
    behavior: classical
    path: "./rule_provider/xl-akrab.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/Openclash/main/Backup/rule_provider/xl-akrab.yaml
    interval: 86400
#
#
# ================= RULE SET REJECT =================
  Reject:
    type: file
    behavior: classical
    path: "./rule_provider/reject.yaml"
  rule_ABPindo:
    type: http
    behavior: classical
    path: "./rule_provider/rule_ABPindo.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_ABPindo.yaml
    interval: 43200
  rule_AdAway:
    type: http
    behavior: classical
    path: "./rule_provider/rule_AdAway.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_AdAway.yaml
    interval: 43200
  rule_Malicious-URLhaus:
    type: http
    behavior: classical
    path: "./rule_provider/rule_Malicious-URLhaus.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_Malicious-URLhaus.yaml
    interval: 43200
  rule_NoCoin-filter:
    type: http
    behavior: classical
    path: "./rule_provider/rule_NoCoin-filter.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_NoCoin-filter.yaml
    interval: 43200
  rule_oisd-small:
    type: http
    behavior: classical
    path: "./rule_provider/rule_oisd-small.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_oisd-small.yaml
    interval: 43200
  rule_Phishing-URL:
    type: http
    behavior: classical
    path: "./rule_provider/rule_Phishing-URL.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_Phishing-URL.yaml
    interval: 43200
  rule_ShadowWhisperer-Malware:
    type: http
    behavior: classical
    path: "./rule_provider/rule_ShadowWhisperer-Malware.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_ShadowWhisperer-Malware.yaml
    interval: 43200
  rule_Stalkerware: # Untuk Android+iOS
    type: http
    behavior: classical
    path: "./rule_provider/rule_Stalkerware.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_Stalkerware.yaml
    interval: 43200
  rule_StevenBlackList: #block: fakenews+gambling
    type: http
    behavior: classical
    path: "./rule_provider/rule_StevenBlackList.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_StevenBlackList.yaml
    interval: 43200
  rule_custom:
    type: http
    behavior: classical
    path: "./rule_provider/rule_custom.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/Openclash/main/Backup/rule_provider/rule_custom.yaml
    interval: 43200
#
#
#================= PROXY PROVIDERS =================
proxy-providers:
  Proxy-SG:
    type: file
    path: "./proxy_provider/SG server.yaml"
    health-check:
      enable: true
      url: http://cp.cloudflare.com/generate_204
      interval: 30
  Proxy-ID:
    type: file
    path: "./proxy_provider/ID server.yaml"
    health-check:
      enable: true
      url: http://www.gstatic.com/generate_204
      interval: 30
#
#
#================= PROXY GROUPS =================
proxy-groups:
- name: SG
  type: fallback
  disable-udp: false
  use:
  - Proxy-SG
  url: http://cp.cloudflare.com/generate_204
  interval: '30'
- name: ID
  type: fallback
  disable-udp: true
  use:
  - Proxy-ID
  url: http://www.gstatic.com/generate_204
  interval: '30'
#
#
#================ DNS + FALLBACK-FILTER =================
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  listen: 0.0.0.0:7874
  fake-ip-filter:
    - "+.*"
  nameserver:
  - 1.1.1.1
  - 8.8.8.8
  - 9.9.9.9
  fallback:
  - 1.1.1.1
  - 8.8.8.8
  - 9.9.9.9
  default-nameserver:
  - 8.8.8.8
  - 8.8.4.4
  - 1.1.1.1
  - 1.0.0.1
redir-port: 7892
tproxy-port: 7895
port: 7890
socks-port: 7891
mixed-port: 7893
mode: rule
log-level: silent
allow-lan: true
external-controller: 0.0.0.0:9090
secret: reyre
bind-address: "*"
external-ui: "/usr/share/openclash/ui"
ipv6: false
tun:
  enable: true
  stack: system
  device: utun
  auto-route: false
  auto-detect-interface: false
  dns-hijack:
  - tcp://any:53
profile:
  store-selected: true
  store-fake-ip: true
rules:
- RULE-SET,Direct,DIRECT
- RULE-SET,xl-akrab,DIRECT
- RULE-SET,Reject,REJECT
- RULE-SET,rule_ABPindo,REJECT
- RULE-SET,rule_AdAway,REJECT
- RULE-SET,rule_Malicious-URLhaus,REJECT
- RULE-SET,rule_NoCoin-filter,REJECT
- RULE-SET,rule_oisd-small,REJECT
- RULE-SET,rule_Phishing-URL,REJECT
- RULE-SET,rule_ShadowWhisperer-Malware,REJECT
- RULE-SET,rule_Stalkerware,REJECT
- RULE-SET,rule_StevenBlackList,REJECT
- RULE-SET,rule_custom,REJECT
- MATCH,GLOBAL
unified-delay: true
tcp-concurrent: true
```
