#!/usr/bin/env python
from lib.python.stream_crawler.modules.youtube import Youtube
from lib.python.stream_crawler.modules.twitch import Twitch

class StreamCrawler:
    def run(site):
        if site == 'youtube':
            Youtube()
        elif site == 'twitch':
            Twitch()
        else:
            Youtube()
            Twitch()
