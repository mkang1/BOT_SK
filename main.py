import discord, yaml
import steamapi.response as response
from discord.ext import tasks
import constants # secrets

client = discord.Client()

# @tasks.loop(seconds=5)
# async def callum_counter():
#     channel = client.get_channel(203684985184452609)
#     await channel.send("hi")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # callum_counter.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!playtime'):
        if message.mentions:
            hit = False
            for u in message.mentions:
                if u.id in userList:
                    hit = True
                    steamID = userList[u.id]
                    r = response.playtime(steamID)
                    await message.channel.send(f"{u.name} has played {r} hours of Lost Ark (steamID: {steamID})")
            if hit == False:
                await message.channel.send(f"User {u.name} is not in the monitor list")
        else:
            await message.channel.send("Please specify a user")


token = constants.BOT_SK_TOKEN
with open("steamapi/users.yml", "r") as data:
    userList = yaml.safe_load(data)
client.run(token)