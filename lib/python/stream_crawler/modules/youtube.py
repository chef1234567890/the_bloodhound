#!/usr/bin/env python
from apiclient.discovery import build
import yaml

class Youtube:
    secrets = yaml.load(open('./config/secrets.yml'), Loader=yaml.FullLoader)
    api_key = secrets['youtube']['api_key']
    youtube_client = build('youtube', 'v3', developerKey=api_key)
    channel_list = yaml.load(open('./config/channel_list.yml'), Loader=yaml.FullLoader)

    def crawl(self):
        video_on_live = []
        for channel_id in self.channel_list.values():
            videos = self.youtube_client.search().list(
                part='snippet',
                channelId=channel_id,
                maxResults=5,
                order='date'
            ).execute()

            for video in videos['items']:
                if video['snippet']['liveBroadcastContent'] == 'live':
                    video_on_live.append(video['id']['videoId'])

        return video_on_live
