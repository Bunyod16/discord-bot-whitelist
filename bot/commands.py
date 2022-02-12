from discord.ext import commands
from datetime import datetime
from utils import channel_id, whitelist_roles, now, admins
from database import add_wallet, get_wallet, update_wallet, db_export_excel, db_export_cleanup
import messages
import discord
import os

def is_correct_channel(message):
	if (message.channel.id == channel_id):
		return (1)
	return (0)

def is_admin(message):
	if (message.author.id in admins):
		return (1)
	return (0)

def get_channel_name(message):
	try:
		channel = discord.utils.get(message.guild.channels, id=channel_id)
	except:
		return (0)
	return (channel)

def has_whitelist_role(message):
	roles = message.author.roles
	for role in roles:
		if role.name in whitelist_roles:
			return (1)
	return (0)

def valid_addr(addr):
	addr = str(addr)
	if (not addr.startswith("addr1")):
		return 0
	if (len(addr) != 103):
		return 0
	return 1

class general_commands(commands.Cog):
	
	@commands.command()
	async def whitelist(self, message, *args):
		if	(not is_correct_channel(message) and not is_admin(message)):
			channel = get_channel_name(message)
			if (not channel):
				await message.channel.send(f"Sorry, you can't use my commands in the DM.")
				return 
			await message.reply(f"Please use me in the `#{channel.name}` channel")
			return
		if (len(args) != 1):
			await message.reply(messages.whitelist_example)
			return

		wallet_addr = args[0]
		if (not valid_addr(wallet_addr)):
			await message.reply("To me it seems, this address is invalid!")
			emoji = '❌'
		elif (not has_whitelist_role(message)):
			emoji = '❌'
			await message.reply("Sadly you don't have a whitelist role.")
		else:
			emoji = '✅'
			if (not get_wallet(message.author.id).fetchall()):
				if (not add_wallet( wallet_addr, message.author.id, message.author.name, str(now()))):
					emoji = '❌'
			else:
				if not (update_wallet(wallet_addr, message.author.id, message.author.name, str(now()))):
					emoji = '❌'
		await message.message.add_reaction(emoji)

	@commands.command()
	async def check(self, message, *args):
		result = get_wallet(message.author.id).fetchall()
		if	(not result):
			await message.reply(messages.get_check_message_notwl())
		else:
			await message.reply(messages.get_check_message_wl(result[0][0]))

	@commands.command()
	async def help(self, message):
		if	(is_correct_channel(message)):
			await message.channel.send(embed=messages.get_help_message())
			return
		channel = get_channel_name(message)
		await message.reply(f"Please use me in the `#{channel.name}` channel")

	@commands.command()
	async def excel(self, message):
		if (is_admin(message)):
			db_export_excel()
			await message.channel.send(file=discord.File('./whitelist.xlsx'))
			db_export_cleanup()
		return
