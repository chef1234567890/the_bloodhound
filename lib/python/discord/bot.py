#!/usr/bin/env python
import os

import pandas as pd
import yaml
import discord

from lib.python.common.common import Common

# ToDo: クラス化
# class DiscordBot():
secrets = yaml.load(open('./config/secrets.yml'), Loader=yaml.FullLoader)
token = secrets['discord']['token']
channel_name = '仮設住宅'
discord_client = discord.Client()
base_uri = 'https://www.youtube.com/watch?v='

def get_channel(channel_name):
    for channel in discord_client.get_all_channels():
        if channel.name == channel_name:
            return channel

def get_started_lives():
    started_lives = Common.diff()
    return started_lives

@discord_client.event
async def on_ready():
    channel = get_channel(channel_name)
    started_lives = get_started_lives()
    for started_live in started_lives:
        await channel.send(base_uri + started_live)
    await discord_client.logout()

def run():
    discord_client.run(token)
