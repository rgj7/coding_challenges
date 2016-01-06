"""
CodeAbbey, Problem 176
Coded by whoisrgj
"""

import requests

url = "http://codeabbey.sourceforge.net/say-100.php"
token = input()
payload = {'token': token}
r = requests.post(url, data=payload)

payload['answer'] = 100-int(r.text.split(':')[1].strip())
r = requests.post(url, data=payload)

print(r.text)