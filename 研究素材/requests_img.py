import json
from bs4 import BeautifulSoup
from discord.embeds import Embed
from discord.utils import parse_time
import requests
import discord
from discord.ext import commands
import random

with open("rss.json", 'r',encoding="utf-8") as reader:
    jdd = json.load(reader)

intents = discord.Intents.all()

intents.members = True

bot = commands.Bot(command_prefix='.',intents=intents)

bot.remove_command('help')

@bot.event  
async def on_ready():
    print('online')

@bot.command()
async def sd(ctx):
    response = requests.get("https://www.cdc.gov.tw/Bulletin/Detail/E7bi2j8UYj1Rmz73OPE7Yg?typeId=9")
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.find_all("img", {"class": "img-thumbnail"}, limit=5)
    image_links = [result.get("src") for result in results] 
    for index, link in enumerate(image_links):
        tr = 'https://www.cdc.gov.tw/{}'.format(link)
    embed = discord.Embed(title='',description='',color=random.randint(0000000,9999999))
    embed.set_author(name='{}'.format(bot.user.name), url='', icon_url='{}'.format(bot.user.avatar_url))
    embed.set_image(url='https://www.cdc.gov.tw//Uploads/5f717e34-7d28-403f-ae6e-1fe31381275d.PNG')
    await ctx.send(embed=embed)

bot.run(jdd['discord token'])