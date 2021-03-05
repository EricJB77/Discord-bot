
import discord
import os
import random
from stay_awake import stay_awake

bot = discord.Client()

bunny_list = [
  "https://media1.giphy.com/media/3o6Zt481isNVuQI1l6/200.gif",
  "https://i.pinimg.com/originals/62/d1/81/62d1811698581fab04b6767a1398829b.gif"
]

@bot.event
async def on_ready():
  print("We have logged on as {0.user}".format(bot))

@bot.event
async def on_message(message):
  print("Recevied message")
  if message.author == bot.user:
    return

  if message.content.startswith("hi"):
    await message.channel.send(random.choice(bunny_list))
  else:
    await message.channel.send("Why don't you greeet me?")

stay_awake()
bot.run(os.getenv('TOKEN'))
