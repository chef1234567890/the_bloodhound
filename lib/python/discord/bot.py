#!/usr/bin/env python

import discord
import yaml


class Bot:
    secrets = yaml.load(open('./config/secrets.yml'), Loader=yaml.FullLoader)
    print(secrets)
    token = secrets['discord']['token']
    channel_id =　secrets['discord']['channel_id']
    discord_client = discord.Client()

    @discord_client.event
    async def on_ready():
        print('Bloodhound is ready.')

    discord_client.run(token='a')
