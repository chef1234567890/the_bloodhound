#!/usr/bin/env python
import shutil
import csv

from lib.python.stream_crawler.modules.youtube import Youtube
from lib.python.stream_crawler.modules.twitch import Twitch
#from lib.python.discord.bot import DiscordBot
from lib.python.discord import bot
from lib.python.common.common import Common


class StreamCrawler:
    def run(site):
        if site == 'youtube':
            videos_on_live = Youtube().crawl()
        else:
            videos_on_live = Twitch().crawl()

        if videos_on_live:
            shutil.move('./tmp/recent.cache', './tmp/previous.cache')
            with open('./tmp/recent.cache', 'w') as f:
                recent_cache = csv.writer(f, lineterminator='\n')
                recent_cache.writerow(videos_on_live)
            diff = Common.diff()
            if diff:
                bot.run()
