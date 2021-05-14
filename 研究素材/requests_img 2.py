import requests
from lxml import html
 
rss = requests.get("https://www.cdc.gov.tw/Bulletin/Detail/3Bp_133jaKM_9c3TecbuTQ?typeId=9")

tt = html.fromstring(rss.text)

img = tt.xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/img")[0]

print(img.attrib['src'])