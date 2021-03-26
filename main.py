import discord
import os
import tasks
from discord.ext import commands
from keep_alive import keep_alive

#client = discord.Client()


client = commands.Bot(command_prefix='$')



@client.command()
async def quote(msg):
    await msg.send(tasks.quote())

@client.command()
async def teachme(msg, *, args):
  languages ={
    777575121937235969: "la",
    777575200853196872: "ja",
    777575237465538612: "fr",
    777603855127019531: "de",
    777603883110629408: "es",
    787649103273918464: "sw"
  }
  if msg.channel.id not in languages:
    language = None
  else:
    language = languages[msg.channel.id]

  answer = tasks.teachme(args, language)
  await msg.send(answer[1])
  await msg.send(answer[0])


@client.command()
async def product(msg, *args: int):
  answer = int(1)
  for num in args:
    answer *= num
  await msg.send(answer)



keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))

#ja == japanese
#la = latin
#fr = french
#de = german
#es = spanish
#sw = Swahili