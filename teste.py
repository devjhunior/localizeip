import requests

resp = requests.get(f'https://ipinfo.io/192.168.1.64?token=89bdb9e2ed33ff')
print(resp.content["bogon"])