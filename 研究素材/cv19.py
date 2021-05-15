import requests

c = requests.get('https://covid19dashboard.cdc.gov.tw/dash3')
cc = c.json()
a = cc['0']['確診']
b = cc['0']['死亡']
print('台灣確診人數{}\n台灣死亡人數{}'.format(a,b))