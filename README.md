# Taiwan_COVID-19_RSS
利用台灣衛生福利部官網的RSS服務發送即時訊息至Discord

前置準備
================
安裝 [Python 3.9][Python-url] 

提示: 
1. 安裝python時，記得要打勾「Add python 3.9 to PATH」 
2. 點選 「Customize installation」 
3. 把 「pip」選項打勾 
4. 直接按「Next」「Install」直接安裝 

[Python-url]:https://www.python.org/

安裝程式庫
----------

discord.py

    # Windows
    pip install discord.py
  
    # Linux
    python3 pip install discord.py

feedparser

    # Windows
    pip install feedparser
  
    # Linux
    python3 pip install feedparser

requests

    # Windows
    pip install requests
  
    # Linux
    python3 pip install requests

lxml

    # Windows
    pip install lxml
    
    #Linux
    python3 pip install lxml

資料部屬
================
需要更動`rss.json`內部資料

    {
    "post_list": "richie code!",
    "channel": "discord text channel",
    "discord token": "token"
    }

`post_list` : 存取用，無須更動 

`channel` : Discord文字頻道ID 

(取得文字房ID方式首先進入你的伺服器，選擇一個文字頻道後點滑鼠右鍵，點擊「複製ID」並複製到「`discord text channel`」即可) 

`discord token` :  Discord機器人令牌，以下教學範例 

1. 點擊[這裡][discord-developers]並登入您的帳號 
2. 點擊「New Application」輸入名稱(名稱需2~128個字) 
3. 點擊「Bot」後再點擊「Add Bot」
4. 點擊後會顯示「ADD A BOT TO THIS APP?」，請選擇「Yes, do it!!」 
5. 到「TOKEN」點擊「Copy」複製令牌 
6. 將複製到的令牌貼到「`token`」裡 
7. 回到瀏覽器點擊「OAuth2」後，下滑到「OAuth2 URL Generator」的「SCOPES」點擊「bot」
8. 點擊後下面會出現「BOT PERMISSIONS」，點擊「Administrator」(管理員)後會在「SCOPES」出現一串連結
9. 點擊「Copy」後再瀏覽器貼上連結
10. 之後選擇要加入哪個伺服器，按確定就完成了!

[discord-developers]:https://discord.com/developers/applications

(如果建立失敗並出現「Too many users have this username, please try another」,純屬名字已有人使用，請到「General Information」重新命名) 

以上都完成後記得存檔，點擊「covid19_RSS.py」如果沒有閃退並顯示

    (你的機器人名稱) Bot
    已定位 (你的文字頻道) 頻道
    >> 疫情RSS啟動成功 <<
    疫情Ran if

就大功告成了!

聲明
----------
「全部程序使用`中央疫情指揮中心`RSS擷取疫情訊息」 

「此程序無須版權申請且資源都是公開的，您可以放心使用」

「此程序非萬能，請不要過度依賴!」

「請不要相信來路不明的網路訊息!!想知道更及時的疫情情報，請上[中央疫情指揮中心][cdc]官網了解更多詳細信息」 

[cdc]:https://www.cdc.gov.tw/
預覽圖
===========
![image](https://user-images.githubusercontent.com/51959827/118259288-8fea3980-b4e3-11eb-8c93-09ea1f41bd4a.png)
![image](https://user-images.githubusercontent.com/51959827/118283670-31808380-b502-11eb-8309-30ff8332ac32.png)

