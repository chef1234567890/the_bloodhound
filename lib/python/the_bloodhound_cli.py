#!/usr/bin/env python
import click

#from lib.python.discord.bot import DiscordBot
from lib.python.discord import bot
from lib.python.stream_crawler.stream_crawler import StreamCrawler

class BloodhoundCLI:
    @click.group()
    def bloodhound_cli():
        pass

    @bloodhound_cli.command()
    #@click.argument('message')
    def discord():
        #DiscordBot().run(message)
        bot.run()

    @bloodhound_cli.command()
    @click.option('--site', type=click.Choice(['youtube', 'twitch', 'all']), required=True)
    def crawl(site):
        StreamCrawler.run(site)
