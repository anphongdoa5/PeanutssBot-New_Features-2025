import nest_asyncio
#from distutils.cmd import Command
from importlib.metadata import requires
from math import perm
from optparse import Option
import os
import random
from sqlite3 import Timestamp
from typing import Any, Text
from unicodedata import name
from urllib import response
import discord, asyncio
from discord import channel
from discord import message
from discord import embeds
from discord import user
from discord import member
from datetime import timedelta
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from dotenv import load_dotenv
from datetime import datetime, timedelta
# from dotenv.main import with_warn_for_invalid_lines
import requests
from discord.utils import get
from discord.ext import commands
import aiohttp
from discord_together import DiscordTogether
import pytz
from typing import List
import wikipedia
from weather import Weather
from deep_translator import GoogleTranslator
from gtts import gTTS
import yt_dlp
from discord.ui import View, Button

#
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#run
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"{client.user.name} đã kết nối tới Discord")
        client.togetherControl = await DiscordTogether(TOKEN)

        activity = discord.Game(name='/ai-chat để đặt câu hỏi với AI', type=3)
        await client.change_presence(status=discord.Status.online, activity=activity)


client = aclient()
tree = app_commands.CommandTree(client)



#commands list


@tree.command(name="help", description = "Xem tất cả các lệnh của bot")
async def self(interaction: discord.Interaction):
    myembed = discord.Embed (title = 'Peanutss Bot (v4.2.0)', description = 'Sử dụng `/[lệnh]` để tương tác với bot', color = discord.Color.gold())
    myembed.set_author (name = "Danh Sách Lệnh")
    myembed.add_field (name = "💬 Tương Tác - (5)", value = "</số-may-mắn:1014044426898784275>, </máy-tính-bỏ-túi:1137034655112106046>, </máy-tính-tuổi-thông-minh:1013757293248122971>, </văn-mẫu:1014047478808576021>, </hành-động:1014047478808576020>", inline=False)
    myembed.add_field (name = "🤖 Trí Tuệ Nhân Tạo (AI) - (2)", value = "`/ai-chat` `/imagine`", inline=False)
    myembed.add_field (name = "🎵 Âm Nhạc - (7)", value = "`/play`, `/skip` ,`/pause`, `/resume`, `/queue`, `/join`, `/leave`", inline=False)
    myembed.add_field (name = "🎮 Mini Game - (2)", value = "`/xì-dách`, `/kéo-búa-bao`", inline=False)
    myembed.add_field (name = "🎁 Media - (7)", value = "</meme:1014044426898784273>, </darkmeme:1014044426898784274>, </girl:1014044427255287884>, </cat:1014044427255287878>, </dog:1014044427255287879>, </food:1014044427255287880>, </waifu:1014044427255287882>", inline=False)
    myembed.add_field (name = "📺 Giải Trí - (6)", value = "</youtube:1014044427255287885>, </cờ-vua:1025980386439856229>, </uno:1139271595504963595>, </gartic-phone:1139271595504963594>, </putt-party:1139271595504963596>, </poker-night:1025980386439856230>", inline=False)
    myembed.add_field (name = "🔞 NSFW - (1)", value = "</hentai:1014044427255287883>", inline=False)
    myembed.add_field (name = "🪙 Tiền Tệ - (1)", value = "</binance:1014044427372744773>", inline=False)
    myembed.add_field (name = "⚠️ Quản Lí Server- (4)", value = "`/kick` `/ban` `/unban` `/clear`", inline=False)
    myembed.add_field (name = "💡 Tính Năng Bổ Trợ - (9)", value = "`/speak` </tìm-tên-bài-hát:1136561727945842729>, </rút-gọn-link:1136680617967362118>, </tạo-qr-code:1136665819800150026>, </dịch:1014044427255287887>, </lyrics:1136404460306956439>, </sắp-tết:1014044427255287886>, </thời-tiết:1025427457559502868>, </chat-with-another-language:1027239217073487923>", inline=False)
    myembed.add_field (name = "⚙️ Guilds - (6)", value = "</tính-năng-mới:1136902132457541703>, </help:1014044426898784271>, </ping:1014044427372744766>, </server-status:1014044427372744771>, </server-avatar:1014044427372744772>, </avatar:1025964029438607421>", inline=False)
    myembed.add_field (name = "☎️ Contact - (3):", value = "</contact:1014044427372744765>, </donate:1014044427372744767>, </invite:1014044427372744770>", inline=False)
    myembed.set_footer(text="• Big Update: Thêm Lệnh 'AI-Chat' giúp tra cứu thông tin một cách chính xác hơn!")
    await interaction.response.send_message(embed = myembed, ephemeral = False)
    

#
@tree.command(name="máy-tính-tuổi-thông-minh", description = "Dùng để tính toán tuổi của bạn")
async def self(interaction: discord.Interaction, nhap_tuoi: str):
    await interaction.response.send_message(f"Bạn đã {nhap_tuoi} tuổi rồi", ephemeral = False)

#

@tree.command(name="máy-tính-chiều-cao", description = "Dùng để tính toán chiều cao của bạn (nhập số centimet)")
async def self(interaction: discord.Interaction, nhap_chieu_cao: int):
    await interaction.response.send_message(f"Bạn cao {nhap_chieu_cao}cm ", ephemeral = False)
    
    
######
@tree.command(name="meme", description = "Gửi cho bạn một meme")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as r:
            memes = await r.json()
            memeembed = discord.Embed(color = discord.Color.green())
            memeembed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            memeembed.set_footer(text=f"Meme của mọi nhà")
    await interaction.response.send_message(embed = memeembed, ephemeral = False)
    rand_func()
    await interaction.response.send_message(embed = memeembed, ephemeral = False)
######
@tree.command(name="darkmeme", description = "Gửi cho bạn một darkmeme")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/dankmemes/new.json?sort=hot") as r:
            darkmemes = await r.json()
            darkembed = discord.Embed(color = discord.Color.red())
            darkembed.set_image(url=darkmemes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            darkembed.set_footer(text=f"Đảk Mêm")
    await interaction.response.send_message(embed = darkembed, ephemeral = False)

######
@tree.command(name="số-may-mắn", description = "Cho bạn một con số may mắn trong ngày")
async def self(interaction: discord.Interaction):
    lknum = random.randint(1,99)
    peabot_rep = 'Con số may mắn hôm nay của bạn là: ' + str(lknum) + ' 🥳' 

    await interaction.response.send_message(f'{peabot_rep}\n Nhớ cầm lấy nó đi đánh đề nhé XD ^^')

######
@tree.command(name="cat", description = "Gửi cho bạn một tấm hình mèo")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
    #api đuồi bầu gắn url trong 1 list, phải tách bằng 1 int chứ không thể tách như thường
        async with cs.get("https://api.thecatapi.com/v1/images/search") as r:
            cats = await r.json()

            catch = cats[0] #trả về dãy như api thường (mất [])
            catlink = catch['url'] #tách data như thường

            catembed = discord.Embed(color = discord.Color.blue())
            catembed.set_image(url=catlink)
            catembed.set_footer(text=f"Mèo méo meo mèo meo")
        
    await interaction.response.send_message(embed = catembed, ephemeral = False)


######
@tree.command(name="dog", description = "Gửi cho bạn một bức hình chó")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
            dogs = await r.json()
            dogsembed = discord.Embed(color = discord.Color.gold())
            dogsembed.set_image(url=dogs["message"])
            dogsembed.set_footer(text=f"Cute Dogs :3")
    await interaction.response.send_message(embed = dogsembed, ephemeral = False)


######
@tree.command(name="food", description = "Gửi cho bạn một bức hình toàn là đồ ăn")
async def self(interaction: discord.Interaction):       
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/food/new.json?sort=hot") as r:
            foods = await r.json()
            foodsembed = discord.Embed(color = discord.Color.green())
            foodsembed.set_image(url=foods["data"]["children"][random.randint(0, 25)]["data"]["url"])
            foodsembed.set_footer(text=f'Mlem mlem')
    await interaction.response.send_message(embed = foodsembed, ephemeral = False)

######
@tree.command(name="waifu", description = "Gửi cho bạn một bức hình waifu")
async def self(interaction: discord.Interaction):       
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://api.waifu.pics/sfw/waifu") as r:
            waifu = await r.json()
            waifuembed = discord.Embed(color = discord.Color.dark_orange())
            waifuembed.set_image(url=waifu["url"])
            waifuembed.set_footer(text=f"Who is your waifu? ❤️")
    await interaction.response.send_message(embed = waifuembed, ephemeral = False)


######
@tree.command(name="hentai", description = "Lệnh chỉ được dùng trong phòng có tag NSFW 'waifu', 'neko', 'blowjob'", nsfw = 'true')
async def hentai(interaction: discord.Interaction, style: str):
        link = "https://api.waifu.pics/nsfw/"
        fullurl = link + style
        async with aiohttp.ClientSession() as cs:
            async with cs.get(fullurl) as r:
                nsfw = await r.json()
                nsfwembed = discord.Embed(color = discord.Color.dark_red())
                nsfwembed.set_image(url=nsfw["url"])
                nsfwembed.set_footer(text=f"⚠️| Not Safe For Work!!")
                await interaction.response.send_message(embed = nsfwembed, ephemeral = False)


@hentai.autocomplete('style')
async def hentai_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    style = ['waifu','neko','blowjob']
    return [
        app_commands.Choice(name=stl, value=stl)
        for stl in style if current.lower() in stl.lower()
        ]

#######
@tree.command(name="girl", description = "Gửi cho bạn những bức hình thattuoimat❤️")
async def self(interaction: discord.Interaction):

    lines = open('list_girl.txt').read().splitlines()
    link = random.choice(lines)
   
    girlembed = discord.Embed(color = discord.Color.from_rgb(255,105,180))
    girlembed.set_image(url=link)
    girlembed.set_footer(text=f"Mỗi bức ảnh, một niềm vui ❤️")
    await interaction.response.send_message(embed = girlembed, ephemeral = False)


@tree.command(name="youtube", description = "Xem Youtube trực tiếp trên Discord")
async def youtube(interaction: discord.Interaction): 
    try:
        voice_id = interaction.user.voice.channel.id
        link = await client.togetherControl.create_link(voice_id, 'youtube')
        await interaction.response.send_message(f'Nhấn vào link để xem Youtube: {link}', ephemeral = False)
    except:
        await interaction.response.send_message('❌| Bạn phải vào kênh voice trước!!', ephemeral = False)

###
@tree.command(name="chess", description = "Chơi cờ vua trực tiếp trên Discord")
async def youtube(interaction: discord.Interaction): 
    try:
        voice_id = interaction.user.voice.channel.id
        link = await client.togetherControl.create_link(voice_id, 'chess')
        await interaction.response.send_message(f'Nhấn vào link để tham gia trò chơi: {link}', ephemeral = False)
    except:
        await interaction.response.send_message('❌| Bạn phải vào kênh voice trước!!', ephemeral = False)

###
@tree.command(name="poker-night", description = "Chơi bài poker trực tiếp trên Discord")
async def youtube(interaction: discord.Interaction): 
    try:
        voice_id = interaction.user.voice.channel.id
        link = await client.togetherControl.create_link(voice_id, 'poker')
        await interaction.response.send_message(f'Nhấn vào link để tham gia trò chơi: {link}', ephemeral = False)
    except:
        await interaction.response.send_message('❌| Bạn phải vào kênh voice trước!!', ephemeral = False)


@tree.command(name="sắp-tết", description = "Đếm ngược ngày đến Tết Nguyên Đán")
async def self(interaction: discord.Interaction):   
    #set up ngay den tet
    ngay_tet = datetime.strptime('Feb 17 2025 00:00', '%b %d %Y %H:%M') 
    hom_nay = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) #set timezone về VN
    count = int((ngay_tet - hom_nay.replace(tzinfo=None)).total_seconds())

    #dem ngay gio
    ngay = count//86400
    gio = (count-ngay*86400)//3600
    phut = (count-ngay*86400-gio*3600)//60
    giay = count-ngay*86400-gio*3600-phut*60
    await interaction.response.send_message(f"Chỉ còn **{ngay}** ngày **{gio}** giờ **{phut}** phút **{giay}** giây nữa là đến tết 2023 rồi!!!!", ephemeral = False) 

##########
@tree.command(name = "dịch", description = "Dịch bất cứ ngôn ngữ nào trên thế giới: en, ja, vi,...")
async def translate(interaction: discord.Interaction, input_lang: str, output_lang: str, noidung: str):
    #khai bao language
    if input_lang == "Tiếng Việt":
        in_lang = 'vi'
    if input_lang == "Tiếng Anh":
        in_lang = 'en'
    if input_lang == "Tiếng Nhật":
        in_lang = 'ja'
    if input_lang == "Tiếng Trung (Phồn Thể)":
        in_lang = 'zh-TW'
    if input_lang == "Tiếng Trung (Giản Thể)":
        in_lang = 'zh-CN'
    if input_lang == "Tiếng Indo":
        in_lang = 'id'
    if input_lang == "Tiếng Hàn":
        in_lang = 'ko'
    if input_lang == "Tiếng Thái":
        in_lang = 'th'
    if input_lang == "Tiếng Đức":
        in_lang = 'de'
    if input_lang == "Tiếng Pháp":
        in_lang = 'fr'
    if input_lang == "Tiếng Nga":
        in_lang = 'ru'
    if input_lang == "Tiếng Tây Ban Nha":
        in_lang = 'es'
    if input_lang == "Tiếng Ý":
        in_lang = 'it'

#output lang
    if output_lang == "Tiếng Việt":
        out_lang = 'vi'
    if output_lang == "Tiếng Anh":
        out_lang = 'en'
    if output_lang == "Tiếng Nhật":
        out_lang = 'ja'
    if output_lang == "Tiếng Trung (Phồn Thể)":
        out_lang = 'zh-TW'
    if output_lang == "Tiếng Trung (Giản Thể)":
        out_lang = 'zh-CN'
    if output_lang == "Tiếng Indo":
        out_lang = 'id'
    if output_lang == "Tiếng Hàn":
        out_lang = 'ko'
    if output_lang == "Tiếng Thái":
        out_lang = 'th'
    if output_lang == "Tiếng Đức":
        output_lang = 'de'
    if output_lang == "Tiếng Pháp":
        out_lang = 'fr'
    if output_lang == "Tiếng Nga":
        out_lang = 'ru'
    if output_lang == "Tiếng Tây Ban Nha":
        out_lang = 'es'
    if output_lang == "Tiếng Ý":
        out_lang = 'it'

    result = GoogleTranslator(source=f'{in_lang}', target=f'{out_lang}').translate(text=noidung)
   

    dich_embed = discord.Embed (title = f'Kết quả dịch từ {input_lang} sang {output_lang}:', color = discord.Color.green())
    dich_embed.add_field (name = 'Văn Bản Gốc:', value = noidung, inline = False)
    dich_embed.add_field (name = 'Văn Bản Sau Khi Dịch: ', value = result, inline = False)
    dich_embed.set_footer (text = f'Lệnh được thực hiện bởi: {interaction.user}')
    await interaction.response.send_message(embed = dich_embed, ephemeral = False)

@translate.autocomplete('input_lang')
async def translate_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    input_lang = ['Tiếng Việt', 'Tiếng Anh', 'Tiếng Nhật', 'Tiếng Trung (Phồn Thể)','Tiếng Trung (Giản Thể)', 'Tiếng Indo', 'Tiếng Hàn', 'Tiếng Thái', 'Tiếng Đức', 'Tiếng Pháp', 'Tiếng Nga', 'Tiếng Tây Ban Nha', 'Tiếng Ý']
    return [
        app_commands.Choice(name=lang, value=lang)
        for lang in input_lang if current.lower() in lang.lower()
        ]

@translate.autocomplete('output_lang')
async def translate_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    output_lang = ['Tiếng Việt', 'Tiếng Anh', 'Tiếng Nhật', 'Tiếng Trung (Phồn Thể)','Tiếng Trung (Giản Thể)', 'Tiếng Indo', 'Tiếng Hàn', 'Tiếng Thái', 'Tiếng Đức', 'Tiếng Pháp', 'Tiếng Nga', 'Tiếng Tây Ban Nha', 'Tiếng Ý']
    return [
        app_commands.Choice(name=lang, value=lang)
        for lang in output_lang if current.lower() in lang.lower()
    ]
##########

#
@tree.command(name="contact", description = "Thông tin liên hệ với Developer")
async def self(interaction: discord.Interaction):   
    contactembed = discord.Embed (color = discord.Color.dark_grey())
    contactembed.set_author (name = "Liên hệ với Dev tại:")
    contactembed.add_field (name = "Discord Account ^^:", value = 'Peanuts Is Me (Andy)#2757', inline=False)
    contactembed.add_field (name = "Link Facebook ^^:", value = 'https://facebook.com/yt.andymusic', inline=False)
    contactembed.add_field (name = "Website ^^:", value = 'https://peanutssbot.tk', inline=False)
    contactembed.add_field (name = "Link Youtube ^^:", value = 'https://youtube.com/c/andymusicc', inline=False)
    contactembed.add_field (name = "Github:", value = 'https://github.com/anphongdoa5', inline=False)
    await interaction.response.send_message(embed = contactembed, ephemeral = False)

#
@tree.command(name="ping", description = "Kiểm tra độ trễ của bot")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Độ trễ của tớ là {round(client.latency * 1000)}ms')

#
@tree.command(name="donate", description = "Ủng hộ Developer một vài ly cafe")
async def self(interaction: discord.Interaction):
    donateembed = discord.Embed (title = 'Các phương thức ủng hộ:', color = discord.Color.orange())
    donateembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/854951941472911361/1119843698390347836/IMG_3315.png')
    donateembed.set_author (name = "Donate ủng hộ Dev ly cà phê tại đây (quét mã QR bên cạnh hoặc link bên dưới):")
    donateembed.add_field (name = "Playerduo:", value = 'https://playerduo.net/peanutss', inline=False)
    donateembed.add_field (name = "Paypal: `@andyhnh`", value = 'https://www.paypal.me/andyhnh', inline=False)
    donateembed.set_footer(text="Cảm ơn bạn rất nhiều <3 / Luv u guys so much <3")
    await interaction.response.send_message(embed = donateembed, ephemeral = False)

#
@tree.command(name="covid19vn", description = "Xem tình hình, diễn biến dịch COVID-19 tại Việt Nam")
async def self(interaction: discord.Interaction):
    response = requests.get('http://coronavirus-19-api.herokuapp.com/countries/vietnam')
    data = response.json()
    cases = data['cases']
    deaths = data['deaths']
    recovered = data['recovered']
    peabot_rep = f"TÌNH HÌNH COVID 19 TẠI VIỆT NAM:\n☣  Số Người Nhiễm: {cases} người\n💀  Số Người Tử Vong: {deaths} người\n✅  Số Người Bình Phục: {recovered} người"
    await interaction.response.send_message(peabot_rep, ephemeral = False)

#
@tree.command(name="covid19", description = "Xem tình hình, diễn biến dịch COVID-19 trên toàn thế giới")
async def self(interaction: discord.Interaction):
    response = requests.get('http://coronavirus-19-api.herokuapp.com/countries/world')
    data = response.json()
    cases = data['cases']
    deaths = data['deaths']
    recovered = data['recovered']
    peabot_rep = f"TÌNH HÌNH COVID 19 TRÊN THẾ GIỚI:\n☣  Số Người Nhiễm: {cases} người\n💀  Số Người Tử Vong: {deaths} người\n✅  Số Người Bình Phục: {recovered} người"
    await interaction.response.send_message(peabot_rep, ephemeral = False)

#
@tree.command(name="invite", description = "Lấy link mời bot vào server")
async def self(interaction: discord.Interaction):
    inviteembed = discord.Embed (color = discord.Color.green())
    inviteembed.set_author (name = "Link Invite Peanutss Bot")
    inviteembed.add_field (name = "Link:", value = 'https://discord.com/oauth2/authorize?client_id=728462830407254088&permissions=34631477334&scope=bot', inline=False)
    await interaction.response.send_message(embed = inviteembed, ephemeral = False)

#
@tree.command(name="server-status", description = "Kiểm tra thông tin của server")
async def self(interaction: discord.Interaction):
    statembed = discord.Embed(title=f'Thông tin server {interaction.guild.name} ',description= '', color = discord.Color.from_rgb(147,112,219))
    statembed.set_thumbnail(url=f'{interaction.guild.icon}')

    statembed.add_field(name='Tên Server:', value=f'{interaction.guild.name}', inline=True)
    statembed.add_field(name='Số Lượng Thành Viên:', value=f'{interaction.guild.member_count} thành viên', inline=True)
    statembed.add_field(name='Chủ Server:', value=f'<@{interaction.guild.owner_id}>', inline=True)
    statembed.add_field(name='Server Tạo Lúc:', value=f'{interaction.guild.created_at.strftime("%#d %B %Y, %H:%M")}')

    statembed.add_field(name='Trạng Thái Bot:', value='🟢 Online!!', inline = True)
    statembed.add_field(name='Latency:', value=f'Độ trễ bot: {round(client.latency * 1000)}ms', inline=True)
    statembed.set_footer(text=f'Bởi: {interaction.user}!')

    await interaction.response.send_message(embed = statembed, ephemeral = False)

#
@tree.command(name="server-avatar", description = "Xem ảnh đại diện của server")
async def self(interaction: discord.Interaction):
    avaembed = discord.Embed(title=f'Avatar của server {interaction.guild.name}', description='', color = discord.Color.from_rgb(0,201,87))
    avaembed.set_image(url=f'{interaction.guild.icon}')
    avaembed.set_footer(text=f'Bởi: {interaction.user}!')
    await interaction.response.send_message(embed = avaembed, ephemeral = False)

#
@tree.command(name = "binance", description = "Kiểm tra giá trị các đồng tiền ảo")
async def binance(interaction: discord.Interaction, coin_name: str):

    if coin_name == "Bitcoin (BTC)":
        coin_position = 0
    if coin_name == "Ethereum (ETH)":
        coin_position = 1
    if  coin_name == "Doge Coin (DOGE)":
        coin_position = 9
    if coin_name == "Shiba Inu (SHIB)":
        coin_position = 11
    if coin_name == "Ethereum Classic (ETC)":
        coin_position = 19
    
    coin_api = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
    tach_json_coin = coin_api.json()
    coin_data = tach_json_coin[coin_position] 
    coin_price = coin_data["current_price"]

    await interaction.response.send_message(f'Tỉ giá đồng **{coin_name}** hiện tại là: **{coin_price} USD/1 {coin_name}**', ephemeral = False)
  
@binance.autocomplete('coin_name')
async def binance_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    coin_name = ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Doge Coin (DOGE)', 'Shiba Inu (SHIB)', 'Ethereum Classic (ETC)']
    return [
        app_commands.Choice(name=binan, value=binan)
        for binan in coin_name if current.lower() in binan.lower()
    ]



#
@tree.command(name = "hành-động", description = "...")
async def action_module(interaction: discord.Interaction, hanh_dong: str, tin_nhan: str):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://api.waifu.pics/sfw/{hanh_dong}") as r:
            action = await r.json()
            actionembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
            actionembed.set_image(url=action["url"])
            actionembed.set_footer(text=f"{tin_nhan} ...❤️")
            await interaction.response.send_message(embed = actionembed, ephemeral = False)

@action_module.autocomplete('hanh_dong')
async def action_module_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    hanh_dong = ['kiss', 'hug', 'cry', 'smile', 'highfive', 'kill', 'pat', 'smug', 'bonk', 'lick', 'awoo', 'blush', 'wave', 'slap']
    return [
        app_commands.Choice(name=act, value=act)
        for act in hanh_dong if current.lower() in act.lower()
    ]

@tree.command(name = "văn-mẫu", description = "Tạo ra những bài văn mẫu có giá trị theo thời gian")
async def action_module(interaction: discord.Interaction):
    peabot_rep = [
        'Bắn CSGO cũng giống như đi từ thiện vậy, cái tâm phải đặt lên đầu',
        'Đặt câu hỏi là tốt nhưng cái gì cũng hỏi thì không',
        'Sau này, chỉ có làm thì mới có ăn. Những cái loại không làm mà đòi có ăn thì chỉ có ăn ||đầu buồi|| ăn ||cứt||',
        'Những cái loại ngủ quá giờ trưa thì không giàu được đâu',
        'Nam tử hán đại trượng phu, đánh nhau không lại ||bú cu|| giảng hòa',
        'Tôi có thằng em sinh năm 96 học Bách Khoa Cơ Khí tay ngang sang học IT...',
        'Hảo hánnnn',    
        'Bao lâu thì bán được 1 tỉ gói mè? Trả lời?',
        'Học đếm: 1 - Ngô Diệc Phàm - 3 - 4 - 5 - 6 - 7...',
        'Bạn không có một chút văn hoá nào, bạn không có một chút đạo đức nào. Tại sao bạn lại dùng lệnh này?? Bạn không đủ tư cách để nói chuyện với tôi',
        'Xin là xin vĩnh biệt cụ',
        'Thế bạn nói xem vì sao mình phải trả lời bạn - Peanutss Chen',
        'Chào em, chị là luật sư của army và đã thu thập đủ bằng chứng em xúc phạm army của công ty bên chị. Em vui lòng xóa bài này sau 30 phút. Nếu sau 30 phút mà em vẫn chưa xóa bài thì bên chị sẽ dùng tới pháp luật và em sẽ bị lôi đầu ra Côn Đảo !',
        'CÁC BẠN NHÂN VIÊN ƠI, CÁC BẠN HỖ TRỢ MÌNH VỚI. CÁC BẠN ƠI CÁC BẠN ĐƯA NHẦM ĐỒ CHO MÌNH CÁC BẠN ƠI. CÁC BẠN NHÂN VIÊN HỖ TRỢ ƠI. CÁC BẠN HỖ TRỢ MÌNH KHÔNG CÁC BẠN ƠI. CÁC BẠN ĐIẾC À CÁC BẠN ƠI HỖ TRỢ MÌNH KHÔNG CÁC BẠN ƠI.',
        'Trong trường hợp anh bị say đắm bởi vẻ đẹp quyến rũ của em (hoặc những vẻ đẹp tương tự của em), anh khẳng định anh không liên hệ bởi bất cứ một cô gái khác nào trong nhóm này, có lẽ trái tim của anh chỉ dành cho em. Anh cũng xin khẳng định anh không hề có thể yêu một cô gái nào khác khi đã yêu em..',
        'Ôi bạn ơi! Bạn sức đề kháng kém là do bạn không chơi đồ đấy bạn ạ, nếu bạn chơi đồ vào thì là đề kháng nó khỏe nó không bao giờ bị ốm đâu bạn ạ, chơi đồ là thuốc bổ mà bạn! Bạn phải nên nhớ nhá, cái viên thuốc bình thường, cái viết thuốc ACID B1 bạn mua có 2 nghìn đc mấy viên đúng k ? Hoặc là 10 nghìn 1 viên, 10 nghìn 1 viên là ACID B1 đấy , đúng không? Thế đây những viên thuốc như viên thuốc kẹo, viên thuốc kim cương, viên thuốc vương liệm này, viên thuốc các kiểu lày thì bạn mua cái đấy vào 500 nghìn 1 viên cơ mà! Chơi cái đấy vào đề kháng nó phải cao hơn chứ bạn! Chơi cái đấy vào nhiều đề kháng mà! Bạn không chơi vào đề kháng bạn kém là phải đấy bạn ạ !',
        'Theo mình thì không nên đăng những bài như thế này. Cái xấu xa, mình phải quên nó đi, cho nó mất dần. K nên nhắc lại. Ng tốt sẽ bị ám ảnh, k tốt cho tinh thần, ng xấu sẽ ghi nhận. Ng k hiểu biết sẽ ghi nhớ. Và nếu nhóm còn đăng nhiều bài như t… thế này thì mình sẽ rời nhóm. Cuộc sống rất ngắn ngủi, tại sao phải để tâm đến điều cần quên đi. Hãy sống tích cực và tươi sáng.'
    ]
    response = random.choice(peabot_rep)
    await interaction.response.send_message(response)


    
######
@tree.command(name="wikipedia", description = "Tìm kiếm thông tin trên Wikipedia")
async def wiki(interaction: discord.Interaction, ngon_ngu: str, noi_dung: str):
    if ngon_ngu == 'Tiếng Việt':
        ngon_ngu = 'vi'
    if ngon_ngu == 'Tiếng Anh':
        ngon_ngu = 'en'
    wikipedia.set_lang(f'{ngon_ngu}')
    try:
        # màu xanh
        r_color = 124
        g_color = 252
        b_color = 0
        result = wikipedia.summary(f"{noi_dung}")
    except:
        # màu đỏ
        r_color = 255
        g_color = 0
        b_color = 0
        result = "Lỗi khi nhập từ khóa! Vui lòng nhập chính xác từ khóa bạn cần tìm"

    wikiembed = discord.Embed(
        title = f'Kết quả tìm kiếm "{noi_dung}" trên Wikipedia:', 
        description = result, 
        color = discord.Color.from_rgb(r_color, g_color, b_color)
        ) 
    wikiembed.set_footer (text = f'Lệnh được sử dụng bởi: {interaction.user}  •  Nội dung được trích từ wikipedia.org')
    try:
        await interaction.response.send_message(embed = wikiembed, ephemeral = False)    
    except:
        await interaction.response.send_message("Hình như có lỗi gì đó rồi!", ephemeral = False)   


@wiki.autocomplete('ngon_ngu')
async def wiki_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    ngon_ngu = ['Tiếng Việt','Tiếng Anh']
    return [
        app_commands.Choice(name=wiki1, value=wiki1)
        for wiki1 in ngon_ngu if current.lower() in wiki1.lower()
        ]



#####

@tree.command(name = 'thời-tiết', description = 'Xem tình hình thời tiết ở bất kì thành phố nào trên thế giới')
async def weather(interaction: discord.Interaction, city_name: str):
    try:
        locate = Weather(city_name)
        wind_speed = locate.wind_speed
        temp = round(locate.temp, 1)
        max_temp = round(locate.temp_max, 1)
        min_temp = round(locate.temp_min, 1)
        humidity = locate.humidity
        uv_point = locate.uv

        if uv_point <= 2:
            warn = 'An Toàn'
            tips = 'Bạn nên sử dụng kính râm và kem chống nắng khi ra ngoài trời!'
            embed_color = discord.Color.green()
        if uv_point > 2 and uv_point <= 5:
            warn = 'Khá Nguy Hiểm'
            tips = 'Bạn nên sử dụng kính râm dùng kem chống nắng và che chắn làn da cẩn thận khi ở ngoài trời nắng!'
            embed_color = discord.Color.yellow()
        if uv_point > 5 and uv_point <= 7:
            warn = 'Nguy Hiểm!'
            tips = 'Ảnh hưởng mạnh đến làn da, hãy dùng kem chống nắng có SPF 15 hoặc cao hơn và che chắn làn da cẩn thận khi ở ngoài trời nắng!'
            embed_color = discord.Color.orange()
        if uv_point > 7:
            warn = 'Cực Kì Nguy Hiểm!!!'
            tips = 'Ảnh hưởng rất mạnh lên làn da nếu không được bảo vệ, tiếp xúc lâu có thể gây ung thư và các bệnh khác về da. Hạn chế ra ngoài nếu khu vực của bạn có mức UV này!'
            embed_color = discord.Color.red() 

        weatherEmbed = discord.Embed(title = f"Thời tiết tại {locate.city} - {locate.country} hiện tại!", color = embed_color)
        weatherEmbed.add_field(name = 'Nhiệt độ:', value = f'{temp} °C', inline = False)
        weatherEmbed.add_field(name = 'Nhiệt độ cao nhất:', value = f'{max_temp} °C', inline = True)
        weatherEmbed.add_field(name = 'Nhiệt độ thấp nhất:', value = f'{min_temp}°C', inline = True)
        weatherEmbed.add_field(name = 'Tốc độ gió:', value = f"{wind_speed} m/s" , inline = False)
        weatherEmbed.add_field(name = 'Độ ẩm:', value = f'{humidity}%', inline = False)
        weatherEmbed.add_field(name = 'Chỉ số UV:', value = f'{uv_point} - {warn}', inline = False)
        weatherEmbed.add_field(name = 'Lời Khuyên:', value = f'{tips}', inline = False)
        weatherEmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/946341795950895104/1025413604712919130/unknown.png')
        weatherEmbed.set_footer(text = f'Dự báo thời tiết • Bởi {interaction.user}')
        await interaction.response.send_message(embed = weatherEmbed)
    except:
        await interaction.response.send_message("Không tìm thấy thành phố bạn yêu cầu", ephemeral = True)
       

#####
@tree.command(name = 'avatar', description = 'Xem avatar của mình hoặc của người khác')
async def avatar(interaction: discord.Interaction, user: discord.Member):
    avatarEmbed = discord.Embed(title = f'Avatar của {user}:', color = discord.Color.gold())
    avatarEmbed.set_image(url = user.avatar)
    avatarEmbed.set_footer(text = f'Lệnh được sử dụng bởi {interaction.user}')
    await interaction.response.send_message(embed = avatarEmbed)


#######
@tree.command(name = 'chat-with-another-language', description = 'Tự động chuyển đổi tin nhắn của bạn sang ngôn ngữ khác mà bạn muốn')
async def cwal(interaction: discord.Interaction, language : str, text : str):

    if language == "Tiếng Việt":
        lang_code = 'vi'
    if language == "Tiếng Anh":
        lang_code = 'en'
    if language == "Tiếng Nhật":
        lang_code = 'ja'
    if language == "Tiếng Trung (Phồn Thể)":
        lang_code = 'zh-TW'
    if language == "Tiếng Trung (Giản Thể)":
        lang_code = 'zh-CN'
    if language == "Tiếng Indo":
        lang_code = 'id'
    if language == "Tiếng Hàn":
        lang_code = 'ko'
    if language == "Tiếng Thái":
        lang_code = 'th'
    if language == "Tiếng Đức":
        lang_code = 'de'
    if language == "Tiếng Pháp":
        lang_code = 'fr'
    if language == "Tiếng Nga":
        lang_code = 'ru'
    if language == "Tiếng Tây Ban Nha":
        lang_code = 'es'
    if language == "Tiếng Ý":
        lang_code = 'it'


    trans_text = GoogleTranslator(source='auto', target=f'{lang_code}').translate(text=text)

    username = interaction.user.nick or interaction.user.name #ưu tiên hiển thị nickname trong server, nếu ko có nick name thì hiện tên

    cwalEmbed = discord.Embed(color = discord.Color.random())
    cwalEmbed.set_author(name = f'{username}:', icon_url = f'{interaction.user.avatar}')
    cwalEmbed.add_field(name = f'{trans_text}', value = '\u200B', inline = False) #\u200B là kí tự trống
    await interaction.response.send_message(embed = cwalEmbed)


@cwal.autocomplete('language')
async def cwal_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    language = ['Tiếng Việt', 'Tiếng Anh', 'Tiếng Nhật', 'Tiếng Trung (Phồn Thể)','Tiếng Trung (Giản Thể)', 'Tiếng Indo', 'Tiếng Hàn', 'Tiếng Thái', 'Tiếng Đức', 'Tiếng Pháp', 'Tiếng Nga', 'Tiếng Tây Ban Nha', 'Tiếng Ý']
    return [
        app_commands.Choice(name=lang123, value=lang123)
        for lang123 in language if current.lower() in lang123.lower()
        ]



####




#### test 
@tree.command(name="traloi", description = "Sử dụng Rep")
async def self(interaction: discord.Interaction, ch: str):

    await interaction.response.send_message("this text will be edited after 4 scds")
    await asyncio.sleep(1)
    
    await interaction.edit_original_response(content="this text will be edited after 3 scds")
    await asyncio.sleep(1)
    
    await interaction.edit_original_response(content="this text will be edited after 2 scds")
    await asyncio.sleep(1)
    
    await interaction.edit_original_response(content="this text will be edited after 1 scds")
    await asyncio.sleep(1)
    #await interaction.response.defer(ephemeral = False)

    #await interaction.followup.send("nối")
    await interaction.edit_original_response(content=f'edited')
    await asyncio.sleep(2)
    await interaction.delete_original_response()
    



###########
@tree.command(name="join", description = "Gọi bot vào phòng voice")
async def join(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message("❌ Bạn phải ở trong một kênh voice để sử dụng lệnh này!", ephemeral=True)
        return

    voice_channel = interaction.user.voice.channel
    voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

    if voice_client and voice_client.is_connected():
        await interaction.response.send_message(f"✅ Bot đã có mặt trong {voice_client.channel.mention}!", ephemeral=True)
    else:
        await voice_channel.connect()
        await interaction.response.send_message(f"✅ Đã tham gia **{voice_channel.mention}**!", ephemeral=False)




#########
@tree.command(name="leave", description="Yêu cầu bot rời khỏi voice chat")
async def leave(interaction: discord.Interaction):
    voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

    if voice_client is not None:  # Kiểm tra xem bot có đang ở trong voice channel không
        await voice_client.disconnect()
        await interaction.response.send_message("👋 Bot đã rời khỏi voice chat!")
    else:
        await interaction.response.send_message("❌ Bot không ở trong voice chat nào cả!")




##
@tree.command(name="speak", description="Dùng để nói trong voicechat khi bạn không có mic")
async def self(interaction: discord.Interaction, van_ban: str):
    username = interaction.user.nick or interaction.user.name  # Lấy nickname, nếu không có thì lấy username

    # Tạo file âm thanh
    sound = gTTS(text=van_ban, lang='vi', slow=False)
    sound.save("tts.mp3")

    if interaction.user.voice is not None:  # Kiểm tra user có đang ở voice channel không
        voice_channel = interaction.user.voice.channel
        voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

        if voice_client is None:  # Nếu bot chưa vào phòng, kết nối vào
            voice_client = await voice_channel.connect()
        elif voice_client.channel != voice_channel:  # Nếu bot đang ở kênh khác, di chuyển sang
            await voice_client.move_to(voice_channel)

        source = await discord.FFmpegOpusAudio.from_probe(
            "tts.mp3", method='fallback', executable="D:/Data/Data/Peanutss Bot Project/peabot-new-features-test/ffmpeg/bin/ffmpeg.exe"
        )

        await interaction.response.send_message(f"**{username} muốn nói rằng:** {van_ban}")
        
        if not voice_client.is_playing():  # Kiểm tra nếu bot chưa phát âm thanh thì phát
            voice_client.play(source)
        else:
            await interaction.followup.send("Bot đang phát âm thanh, vui lòng chờ.")


################## khối lệnh âm nhạc ######################

 # Dictionary để lưu danh sách bài hát theo guild ID
queue = {} 

@tree.command(name="play", description="Phát nhạc từ YouTube bằng từ khóa hoặc link")
async def play(interaction: discord.Interaction, query: str):
    await interaction.response.defer()  # Tránh timeout khi tìm kiếm YouTube

    guild_id = interaction.guild.id
    voice_channel = interaction.user.voice.channel if interaction.user.voice else None
    
    if not voice_channel:
        await interaction.followup.send("❌ Bạn phải tham gia voice channel trước!")
        return
    
    voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

    if not voice_client:
        voice_client = await voice_channel.connect()
    elif voice_client.channel != voice_channel:
        await voice_client.move_to(voice_channel)

    # Xác định query là link hay từ khóa
    ydl_opts = {"format": "bestaudio", "noplaylist": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            if "youtube.com" in query or "youtu.be" in query:
                info = ydl.extract_info(query, download=False)  # Nếu là link, tải thông tin trực tiếp
            else:
                info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]  # Nếu là từ khóa, tìm kiếm video
            url = info["url"]
            title = info["title"]
        except Exception as e:
            await interaction.followup.send(f"❌ Không tìm thấy video nào cho: {query}")
            return
    
    # Thêm bài hát vào hàng đợi
    if guild_id not in queue:
        queue[guild_id] = []
    queue[guild_id].append((url, title))

    await interaction.followup.send(f"🎵 **Đã thêm vào hàng đợi:** {title}")

    # Nếu bot chưa phát nhạc, bắt đầu phát
    if not voice_client.is_playing():
        await play_next_song(voice_client, guild_id, interaction)

async def play_next_song(voice_client, guild_id, interaction):
    if guild_id in queue and queue[guild_id]:
        url, title = queue[guild_id].pop(0)

        ffmpeg_options = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
            "executable": "D:/Data/Data/Peanutss Bot Project/peabot-new-features-test/ffmpeg/bin/ffmpeg.exe"
        }
        
        source = discord.FFmpegOpusAudio(url, **ffmpeg_options)

        def after_play(error):
            if error:
                print(f"Lỗi phát nhạc: {error}")
            asyncio.run_coroutine_threadsafe(play_next_song(voice_client, guild_id, interaction), interaction.client.loop)

        voice_client.play(source, after=after_play)

        await interaction.followup.send(f"🎶 **Đang phát:** {title}")
    else:
        await interaction.followup.send("✅ Hàng đợi đã phát hết, bot sẽ rời voice chat.")
        await voice_client.disconnect()

@tree.command(name="skip", description="Bỏ qua bài hát đang phát hiện tại")
async def skip(interaction: discord.Interaction):
    voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

    if voice_client and voice_client.is_playing():
        voice_client.stop()  # Dừng bài hiện tại, sẽ tự phát bài tiếp theo
        await interaction.response.send_message("⏭ **Đã bỏ qua bài hát!**")
    else:
        await interaction.response.send_message("❌ Không có bài nào đang phát.")

@tree.command(name="pause", description="Tạm dừng bài hát đang phát/")
async def pause(interaction: discord.Interaction):
    voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await interaction.response.send_message("⏸ **Đã tạm dừng nhạc!**")
    else:
        await interaction.response.send_message("❌ Không có bài nào đang phát.")

@tree.command(name="resume", description="Tiếp tục phát nhạc")
async def resume(interaction: discord.Interaction):
    voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await interaction.response.send_message("▶️ **Tiếp tục phát nhạc!**")
    else:
        await interaction.response.send_message("❌ Nhạc chưa bị tạm dừng hoặc không có bài nào để tiếp tục.")

@tree.command(name="queue", description="Xem danh sách bài hát trong hàng chờ")
async def show_queue(interaction: discord.Interaction):
    guild_id = interaction.guild.id

    if guild_id in queue and queue[guild_id]:
        queue_list = "\n".join([f"{i+1}. {title}" for i, (_, title) in enumerate(queue[guild_id])])
        await interaction.response.send_message(f"🎶 **Danh sách bài hát trong hàng chờ:**\n{queue_list}")
    else:
        await interaction.response.send_message("❌ Hàng đợi trống.")



##########
class RPSGame(View):
    def __init__(self, user: discord.User):
        super().__init__(timeout=10)  # Set thời gian chờ 10 giây
        self.user = user
        self.choices = ["✊", "✋", "✌️"]

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.user:
            await interaction.response.send_message("❌ Bạn không phải người chơi của game này!", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="✌️ Kéo", style=discord.ButtonStyle.primary)
    async def rock(self, interaction: discord.Interaction, button: Button):
        await self.process_game(interaction, "✌️")

    @discord.ui.button(label="✋ Bao", style=discord.ButtonStyle.success)
    async def paper(self, interaction: discord.Interaction, button: Button):
        await self.process_game(interaction, "✋")

    @discord.ui.button(label="✊ Búa", style=discord.ButtonStyle.danger)
    async def scissors(self, interaction: discord.Interaction, button: Button):
        await self.process_game(interaction, "✊")

    async def process_game(self, interaction: discord.Interaction, player_choice: str):
        bot_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, bot_choice)

        await interaction.response.edit_message(
            content=f"🆚 Bạn chọn: {player_choice} | Bot chọn: {bot_choice}\n{result}",
            view=None
        )

    def determine_winner(self, player: str, bot: str) -> str:
        if player == bot:
            return "⚖️ **Hòa rồi!**"
        elif (player == "✊" and bot == "✌️") or (player == "✋" and bot == "✊") or (player == "✌️" and bot == "✋"):
            return "🎉 **Bạn thắng!**"
        else:
            return "🤖 **Bot thắng!**"

@tree.command(name="kéo-búa-bao", description="Chơi game Kéo Búa Bao với bot")
async def rps(interaction: discord.Interaction):
    await interaction.response.send_message("🎮 Chọn kéo, búa hoặc bao!", view=RPSGame(interaction.user))




#Bộ bài Xì Lác
CARD_VALUES = {
    "A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10
}
CARD_SUITS = ["♠️", "♥️", "♦️", "♣️"]

def draw_card():
    """ Rút một lá bài ngẫu nhiên """
    rank = random.choice(list(CARD_VALUES.keys()))
    suit = random.choice(CARD_SUITS)
    return f"{rank}{suit}", CARD_VALUES[rank]

def calculate_hand(hand):
    total = 0
    aces = 0
    for card, value in hand:
        if card.startswith("A"):
            aces += 1
            total += 11  # Mặc định Át là 11
        else:
            total += value

    # Nếu tổng điểm vượt quá 21, đổi Át từ 11 thành 1
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

class XiDachGame(View):
    def __init__(self, user: discord.User):
        super().__init__(timeout=30)  # Giới hạn thời gian 30s
        self.user = user
        self.player_hand = [draw_card(), draw_card()]
        self.bot_hand = [draw_card(), draw_card()]

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.user:
            await interaction.response.send_message("❌ Bạn không phải người chơi của game này!", ephemeral=True)
            return False
        return True

    def get_hand_display(self, hand):
        """ Hiển thị bài với emoji lá bài """
        return " | ".join([card for card, _ in hand])

    @discord.ui.button(label="🎯 Rút bài", style=discord.ButtonStyle.primary)
    async def hit(self, interaction: discord.Interaction, button: Button):
        self.player_hand.append(draw_card())
        player_total = calculate_hand(self.player_hand)

        if player_total > 21:
            await interaction.response.edit_message(
                content=f"💥 **Bạn đã rút bài và bị quắc (quá 21 điểm)!**\n\n"
                        f"🃏 **Bài của bạn:** {self.get_hand_display(self.player_hand)} (**{player_total} điểm**)\n"
                        f"🤖 **Bài của nhà cái:** {self.bot_hand[0][0]} | ❓\n"
                        f"❌ **Bạn thua rồi!**",
                view=None
            )
        else:
            await interaction.response.edit_message(
                content=f"🎯 **Bạn đã rút bài!**\n\n"
                        f"🃏 **Bài của bạn:** {self.get_hand_display(self.player_hand)} (**{player_total} điểm**)\n"
                        f"🤖 **Bài của nhà cái:** {self.bot_hand[0][0]} | ❓\n"
                        f"📌 **Bấm 'Dừng' nếu bạn muốn giữ bài!**",
                view=self
            )

    @discord.ui.button(label="🛑 Dừng", style=discord.ButtonStyle.success)
    async def stand(self, interaction: discord.Interaction, button: Button):
        player_total = calculate_hand(self.player_hand)
        bot_total = calculate_hand(self.bot_hand)

        # Bot bốc bài nếu có dưới 16 điểm 
        while bot_total < 16:
            self.bot_hand.append(draw_card())
            bot_total = calculate_hand(self.bot_hand)

        # Xác định kết quả
        if bot_total > 21 or player_total > bot_total:
            result = "🎉 **Bạn thắng!**"
        elif player_total == bot_total:
            result = "⚖️ **Hòa nhau!**"
        else:
            result = "🤖 **Nhà cái thắng!**"

        await interaction.response.edit_message(
            content=f"🃏 **Bài của bạn:** {self.get_hand_display(self.player_hand)} (**{player_total} điểm**)\n"
                    f"🤖 **Bài của nhà cái:** {self.get_hand_display(self.bot_hand)} (**{bot_total} điểm**)\n"
                    f"{result}",
            view=None
        )

@tree.command(name="xì-dách", description="Chơi bài Xì Dách với bot!")
async def xidach(interaction: discord.Interaction):
    game = XiDachGame(interaction.user)
    await interaction.response.send_message(
        f"🃏 **Bắt đầu game Xì Dách!**\n\n"
        f"**Bài của bạn:** {game.get_hand_display(game.player_hand)}\n\n"
        f"**Bài của nhà cái:** {game.bot_hand[0][0]} | ❓\n\n"
        f"🎯 **Bấm 'Rút bài' để bốc thêm hoặc 'Dừng' để giữ bài!**",
        view=game
    )



##################### Khối lệnh quản lý server
@tree.command(name="clear", description="Xóa tin nhắn theo số lượng (tối đa 100).")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, so_luong: int):
    if so_luong <= 0 or so_luong > 100:
        await interaction.response.send_message("❌ Số lượng tin nhắn phải từ **1 đến 100**!", ephemeral=True)
        return

    await interaction.channel.purge(limit=so_luong)
    await interaction.response.send_message(f"✅ Đã xóa **{so_luong}** tin nhắn!", ephemeral=True)


@tree.command(name="kick", description="Kick thành viên ra khỏi server.")
@app_commands.checks.has_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, member: discord.Member, ly_do: str = "Không có lý do"):
    if interaction.user.top_role <= member.top_role:
        await interaction.response.send_message("❌ Bạn không thể kick người có quyền cao hơn hoặc ngang bằng bạn!", ephemeral=True)
        return
    if not interaction.guild.me.guild_permissions.kick_members:
        await interaction.response.send_message("❌ Bot không có quyền `Kick Members`!", ephemeral=True)
        return

    await member.kick(reason=ly_do)
    await interaction.response.send_message(f"✅ **{member.mention} đã bị kick!** 🛑\n**Lý do:** {ly_do}")


@tree.command(name="ban", description="Cấm thành viên khỏi server.")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, ly_do: str = "Không có lý do"):
    if interaction.user.top_role <= member.top_role:
        await interaction.response.send_message("❌ Bạn không thể ban người có quyền cao hơn hoặc ngang bằng bạn!", ephemeral=True)
        return
    if not interaction.guild.me.guild_permissions.ban_members:
        await interaction.response.send_message("❌ Bot không có quyền `Ban Members`!", ephemeral=True)
        return

    await member.ban(reason=ly_do)
    await interaction.response.send_message(f"🚫 **{member.mention} đã bị ban!** 🔨\n**Lý do:** {ly_do}")


client.run(TOKEN) 
