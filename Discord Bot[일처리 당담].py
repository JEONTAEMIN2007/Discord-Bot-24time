import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    
    print(client.user.name)
    print("================")
    game = discord.Game('Visual Studio Code')
    await client.change_presence(status=discord.Status.dnd, activity=game)


@client.event
async def on_message(message):
    if message.content == "안녕하세요":
        await message.channel.send("안녕하세요! 반갑습니다!")

    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂㅇ")

    if message.content == "떡상":
        await message.channel.send("구독자! 떡상 가즈아📈")

    if message.content == "나락":
        await message.channel.send("구독자! 나락 가즈아📉")

    if message.content == "서버":
        await message.channel.send("jeontaemin.kro.kr")
        await message.channel.send("위에 있는 도메인은 미니TV구독님의 섭입니다")
        await message.channel.send("huni.r-e.kr")
        await message.channel.send("위에 있는 도메인은 후니님의 섭입니다")

    if message.content == "!도배10회":
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(5회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(10회)")

    if message.content == "!도배20회":
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(5회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(10회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(15회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(20회)")

    if message.content == "!도배30회":
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(5회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(10회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(15회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(20회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(25회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(30회)")

    if message.content == "!도배40회":
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(5회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(10회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(15회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(20회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(25회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(30회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(35회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(40회)")

    if message.content == "!도배50회":
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(5회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(10회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(15회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(20회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(25회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(30회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(35회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(40회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(45회)")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다")
        await message.channel.send("누군가로부터 인해 도배가 작동하였습니다(50회)")


   # if message.content.startswiht("!추방"):
      #  member = message.guild.get_member(int(message.content.split(" ")[1]))
       # await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))




    #if message.content.startswiht("!청소"):
       # number = int(message.content.split(" ")[1])
       # await message.delete()
       # await message.channel.purge(limit=number)
        #await message.channel.send(f"{number}개의 메세지를 삭제했습니다")

@client.event
async def on_member_join(member):
    role = ""
    for i in member.server.roles:
        if i.name == "USER":
            role = i
            break
    await client.add_roles(member, role)
    
access_token = od.environ["BOT_TOKEN"]
client.run("access_token")
