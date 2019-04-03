import discord
import yaml

# class DiscordBot:
discord_client = discord.Client()
secrets = yaml.load(open('./config/secrets.yml'), Loader=yaml.FullLoader)
token = secrets['discord']['token']
channel_name = '仮設住宅'

def get_channel(channel_name):
    for channel in discord_client.get_all_channels():
        if channel.name == channel_name:
            return channel

def get_message():
    return 'All father gave me sight!'

@discord_client.event
async def on_ready():
    message = get_message()
    channel = get_channel(channel_name)
    await channel.send(message)

def run():
    discord_client.run(token)
