import json
import requests
url = 'https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com/name/-1'
data = json.dumps({
    'clanName': '大枫树',
})
headers = {'Content-Type': 'application/json'}
resp = requests.post(url, data=data, headers=headers)
print(resp.status_code)
if resp.status_code == requests.codes.ok:
    resp_data = json.loads(resp.text)
    print(resp_data)