import requests

final_proxies = []
proxy_test_url = 'https://httpbin.org/ip'

with open("proxies.txt", "r") as proxy_file:
    all_proxies = proxy_file.readlines()
    for proxy in all_proxies:
        try:
            print(proxy)
            response = requests.get(proxy_test_url, proxies={"http": proxy, "https": proxy})
            final_proxies.append(proxy)
            print(response.text)
        except Exception as e:
            print(f"Proxy Failed. {e}")

#res = requests.get('https://faucet.ropsten.be/donate/WV98W3a7hYhBRIDPRGk8D/0x9B3C8652Dc3777F9f12D48d56bF69678F3887d4f', proxies=proxies)
#print(res.text)