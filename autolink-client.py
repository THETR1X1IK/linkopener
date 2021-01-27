import discord
from discord.ext import commands
import asyncio
import webbrowser
import sys

channel = 'https://discordapp.com/api/webhooks/753652488443265164/l6JBp2tjMIFodBTnNSwGVYHdpUtK5tzjR3ORiZ2dF_hvBOI9cae4RElEGrJ7AnN0u0Bh'

client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
	print("Logged on as {0}".format(user))

async def on_message(message):
	global channel
	print('message')
	if '!addch' in message.content.lower():
		print('addch')
		channel = message.content.lower().split()[1]
		print(channel)
	if '!exit' in message.content.lower():
		print('exit')
		await message.channel.send('Вы успешно вышли из программы!')
		sys.exit()
	if(channel in str(message.channel.id)):
		qwe = message.content.split()
		for i in range(len(qwe)):
			if 'https://' in qwe[i] or 'http://' in qwe[i]:
				webbrowser.open_new_tab(qwe[i])
				print(opened)


client.run('NjcyNzgxMTg1NzAwNTkzNzAw.XjQeTg.N3lZh4-Gl9HFMJjqv-UXbPVuMhM')

