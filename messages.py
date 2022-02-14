import discord

whitelist_example = """Wrong usage!
Example: `!whitelist wallet_address`"""

def get_check_message_notwl():
  message = "You are not whitelisted yet. Use `!whitelist wallet_address`."
  return (message)

def get_check_message_wl(addr):
  message = f"You are already whitelisted with address : `{addr}`"
  return (message)

def get_help_message():
  title = "Ugly Secretary's abilities"
  description = ""
  fields = [
    {"name":"!whitelist `wallet_address`", "description":"add your wallet to the whitelist"},
    {"name":"!check", "description":"show your whitelisted address"}
  ]
  message_help = discord.Embed(title=title, description=description, color=0x000000)
  for field in fields:
    message_help.add_field(name=field["name"], value=field["description"], inline=False)
  return (message_help)
