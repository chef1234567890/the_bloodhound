#!/usr/bin/env python
import click

from lib.python.stream_crawler.stream_crawler import StreamCrawler


class BloodhoundCLI:
    @click.group()
    def bloodhound_cli():
        pass

    @bloodhound_cli.command()
    @click.option('--site', type=click.Choice(['youtube', 'twitch']), required=True)
    def crawl(site):
        StreamCrawler.run(site)
