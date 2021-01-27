import discord
from discord.ext import commands
import asyncio
import webbrowser
import sys

channel = 'channel url webhook'

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


client.run('bot token')

