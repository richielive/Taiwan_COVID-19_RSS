import discord
from discord.ext import commands
from discord.ext.tasks import loop
import feedparser
import re
import json
import requests
from lxml import html

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='.',intents=intents)
bot.remove_command('help')
with open("rss.json", 'r',encoding="utf-8") as reader:
    jdd = json.load(reader)

@bot.event  
async def on_ready():
    bot.loop.create_task(random_text())
    channel=bot.get_channel(int(jdd['channel']))
    c = channel.name
    print("{} Bot".format(bot.user))
    print("已定位 {} 頻道".format(c))
    print(">> 疫情RSS啟動成功 <<")

async def random_text():
    update_rss.start()

@loop(seconds=5)
async def update_rss():
    #==========================================RSS==========================================#
    channel=bot.get_channel(int(jdd['channel']))
    d = feedparser.parse('https://www.cdc.gov.tw/RSS/RssXml/Hh094B49-DRwe2RR4eFfrQ?type=1')
    post = d.entries[0]['title']
    link = d.entries[0]['link']
    description = d.entries[0]['description']
    text = re.sub("<.*?>", "", description)
    #=======================================covid-19=======================================#
    c = requests.get('https://covid19dashboard.cdc.gov.tw/dash3')
    cc = c.json()
    a = cc['0']['確診']
    b = cc['0']['死亡']

    try:
        with open("rss.json", 'r',encoding="utf-8") as reader:
            jdata1 = json.loads(reader.read())
            post_list = jdata1['post_list']
        rss = requests.get(link)
        tt = html.fromstring(rss.text)
        img = tt.xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/img")[0]
        imgg = ('https://www.cdc.gov.tw/{}'.format(img.attrib['src']))
        if post != post_list:
            embed=discord.Embed
            embed=discord.Embed(title=f":hourglass::exclamation:**{post}**",url=f"{link}", description=f"{text}\n\n相關新聞請點連結進入\n| 台灣確診人數:{a} | 死亡人數:{b} |",color=5046417)
            embed.set_author(name="{}".format(bot.user.name),url="", icon_url='{}'.format(bot.user.avatar_url))
            embed.set_image(url=imgg)
            embed.set_footer(text="資料來源:衛生福利部疾病管制屬RSS資料中心\n(discord嵌入僅可放一張圖片，更多圖片請點連結)",icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png")
            await channel.send(embed=embed)
            # await channel.send(f'> :hourglass::exclamation:**{post}**\n> {text} \n> {link}')
            with open('rss.json',encoding="utf-8") as r:
                jd = json.load(r)
                jd['post_list'] = post
                json.dump(jd, open("rss.json","w",encoding='utf-8'), indent=4, ensure_ascii=False)
            print('接收到疫情情報!「{}」'.format(post))
        else:
            pass
    except IndexError:
        if (post not in post_list):
            embed=discord.Embed
            embed=discord.Embed(title=f":hourglass::exclamation:**{post}**",url=f"{link}", description=f"{text}\n\n相關新聞請點連結進入\n| 台灣確診人數:{a} | 死亡人數:{b} |",color=5046417)
            embed.set_author(name="{}".format(bot.user.name),url="", icon_url='{}'.format(bot.user.avatar_url))
            embed.set_footer(text="資料來源:衛生福利部疾病管制屬RSS資料中心",icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png")
            await channel.send(embed=embed)
            # await channel.send(f'> :hourglass::exclamation:**{post}**\n> {text} \n> {link}')
            with open('rss.json',encoding="utf-8") as r:
                jd = json.load(r)
                jd['post_list'] = post
                json.dump(jd, open("rss.json","w",encoding='utf-8'), indent=4, ensure_ascii=False)
            print('接收到疫情情報!「{}」'.format(post))
        else:
            pass

bot.run(jdd['discord token'])