from bs4 import BeautifulSoup
import requests
 
response = requests.get("https://www.cdc.gov.tw/Bulletin/Detail/3Bp_133jaKM_9c3TecbuTQ?typeId=9")
soup = BeautifulSoup(response.text, "lxml")
 
results = soup.find_all("img", {"class": "img-thumbnail"}, limit=5)
 
image_links = [result.get("src") for result in results] 

for index, link in enumerate(image_links):
    print(link)