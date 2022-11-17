import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='*',
  self_bot=True
)




@client.event
async def on_connect():

  await client.change_presence(activity = discord.Streaming(name = "I'm lookin' right at the other half of me 👀✨😍" , url = "https://top.gg/bot/813709481430089739"))


keep_alive.keep_alive()
client.run(os.getenv("MTAyMjEwODI4MTc2Mzc5MDg1OA.GxJHka.L3bEf_LKEwXctoFayGs7Aq2NZjgZ4Xnl2WGuco"), bot=False)
