package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"gopkg.in/yaml.v2"
)

const (
	filterFile  = "filter-connectedAkrab.yaml"
	maxAccounts = 40
)

type Proxy struct {
	Name           string `yaml:"name"`
	Server         string `yaml:"server"`
	Port           int    `yaml:"port"`
	Type           string `yaml:"type"`
	UUID           string `yaml:"uuid"`
	AlterID        int    `yaml:"alterId"`
	Cipher         string `yaml:"cipher"`
	TLS            bool   `yaml:"tls"`
	SkipCertVerify bool   `yaml:"skip-cert-verify"`
	Network        string `yaml:"network"`
	WsOpts         struct {
		Path    string            `yaml:"path"`
		Headers map[string]string `yaml:"headers"`
	} `yaml:"ws-opts"`
	XUDP bool   `yaml:"xudp"`
	Key  string `yaml:"key"`
}

func main() {
	url := "https://raw.githubusercontent.com/miracle-desk/Openclash/main/Backup/proxy_provider/filter-akrab.yaml"
	data, err := fetchURL(url)
	if err != nil {
		log.Fatal("Failed to fetch URL:", err)
	}

	proxies, err := parseYAML(data)
	if err != nil {
		log.Fatal("Failed to parse YAML:", err)
	}

	filteredProxies := filterProxies(proxies)
	saveProxies(filteredProxies, filterFile)

	fmt.Println("Successfully saved", len(filteredProxies), "connected accounts with lowest ping to", filterFile)
}

func fetchURL(url string) ([]byte, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("failed to fetch URL: %s", resp.Status)
	}

	data, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	return data, nil
}

func parseYAML(data []byte) ([]Proxy, error) {
	var result map[string][]Proxy
	err := yaml.Unmarshal(data, &result)
	if err != nil {
		return nil, err
	}

	var proxies []Proxy
	for _, list := range result {
		proxies = append(proxies, list...)
	}

	return proxies, nil
}

func filterProxies(proxies []Proxy) []Proxy {
	filteredProxies := make([]Proxy, 0, maxAccounts)
	for i, proxy := range proxies {
		if i >= maxAccounts {
			break
		}
		filteredProxies = append(filteredProxies, proxy)
	}
	return filteredProxies
}

func saveProxies(proxies []Proxy, filename string) {
	output, err := yaml.Marshal(proxies)
	if err != nil {
		log.Fatal("Failed to marshal YAML:", err)
	}

	err = ioutil.WriteFile(filename, output, os.ModePerm)
	if err != nil {
		log.Fatal("Failed to write file:", err)
	}
}
