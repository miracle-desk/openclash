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
    url: https://raw.githubusercontent.com/miracle-desk/openclash/main/backup/rule_provider/xl-akrab.yaml
    interval: 86400
#
#
# ================= RULE SET REJECT =================
  Reject:
    type: file
    behavior: classical
    path: "./rule_provider/reject.yaml"
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
  rule_Malware-Websites:
    type: http
    behavior: classical
    path: "./rule_provider/rule_Malware-Websites.yaml"
    url: https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_Malware-Websites.yaml
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
    url: https://raw.githubusercontent.com/miracle-desk/openclash/main/backup/rule_provider/rule_custom.yaml
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
#  Proxy-fool:
#    type: http
#    url: "https://raw.githubusercontent.com/your_provider.yaml"
#    path: "./proxy_provider/fool-vpn.yaml"
#    interval: 10800
#    health-check:
#      enable: true
#      url: https://cp.cloudflare.com/generate_204
#      interval: 30
  Proxy-filter:
    type: http
    url: "https://raw.githubusercontent.com/your_provider.yaml"
    path: "./proxy_provider/filter-proxies.yaml"
    interval: 10800
    health-check:
      enable: true
      url: https://cp.cloudflare.com/generate_204
      interval: 300
#
#
#================= PROXY GROUPS =================
proxy-groups:
- name: SG
  type: fallback
#  disable-udp: false
  use:
  - Proxy-SG
  url: http://cp.cloudflare.com/generate_204
  interval: '30'
- name: ID
  type: fallback
#  disable-udp: true
  use:
  - Proxy-ID
  url: http://www.gstatic.com/generate_204
  interval: '30'
#- name: fool
#  type: fallback
#  use:
#  - Proxy-fool
#  url: http://cp.cloudflare.com/generate_204
#  interval: '30'
- name: filter
  type: url-test
  use:
  - Proxy-filter
  url: http://cp.cloudflare.com/generate_204
  interval: '30'
# type: fallback, url-test, loadbalance
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
#  - 9.9.9.9
  fallback:
  - 1.1.1.1
  - 8.8.8.8
#  - 9.9.9.9
  default-nameserver:
  - 8.8.8.8
  - 8.8.4.4
  - 1.1.1.1
  - 1.0.0.1
#  - 9.9.9.9
#  - 149.112.112.112
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
#- RULE-SET,xl-akrab,DIRECT
- RULE-SET,Reject,REJECT
- RULE-SET,rule_AdAway,REJECT                   #general
- RULE-SET,rule_Malicious-URLhaus,REJECT        #security
- RULE-SET,rule_Malware-Websites,REJECT         #security
- RULE-SET,rule_Phishing-URL,REJECT             #security
- RULE-SET,rule_ShadowWhisperer-Malware,REJECT  #security
- RULE-SET,rule_Stalkerware,REJECT              #security
- RULE-SET,rule_StevenBlackList,REJECT          #security
- RULE-SET,rule_custom,REJECT                   #general
#================ TORAM ONLINE ===============
#- DST-PORT,30100,DIRECT
#- DOMAIN-KEYWORD,toram,DIRECT
- MATCH,GLOBAL
unified-delay: true
```
