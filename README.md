# the_bloodhound
## Overview
Notify to the discord server ([gmkz](https://discord.gg/4eMqfu)) that a specific streamers have started live stream.
Bloodhand is an interface via discord with the following features:
- Add and delete a monitoring target
- List current monitoring targets
- View the streamers recently streaming live
- and more...

It is only YouTube and Twitch of streaming sites to be monitored.

## architecture
```
                      +-------------------------------------+
                      |           the_bloodhound            |
+-------------+       +-------------+---------+-------------+      +-------------+
| Youtube API | <---  | youtube cli |         | discord cli | ---> | Discord API |
+-------------+       |-------------| handler |-------------|      +-------------+
+-------------+       |-------------|         |-------------|      +-------------+
| Twitch API  | <---  | twitch cli  |         | twitter cli | ---> | Twitter API |
+-------------+       +-------------------------------------+      +-------------+
```
### description
- Discord bot is not usually running.
    - In order to post actively while running, the bot's activation thread needs to loop endlessly.
- First, cron periodically crawls Youtube API and Twitch API.
- Start discord bot and notify if there is a difference (start / end) in live status.

### tree
```
.
├── README.md
├── bin
│   └── the_bloodhound
├── config
│   ├── secrets.yml
│   └── streamers.yml
├── lib
│   └── python
│       ├── discord
│       │   └── bot.py
│       ├── stream_crawler
│       │   ├── modules
│       │   │   ├── twitch.py
│       │   │   └── youtube.py
│       │   └── stream_crawler.py
│       ├── the_bloodhound
│       │   └── diff.py
│       └── the_bloodhound_cli.py
└── requirements.txt
```

## env
### lang
```
the_bloodhound$ pyenv version
3.7.0 (set by /Users/bloodhound/.pyenv/version)
```
- Use discrod.py with python 3.7.x
    - Discord.py(0.16.12) does not support python 3.7.x.
    - In order to use python 3.7.x, need to use discord.py(1.0.0a0) version under development.
    - Ref: https://github.com/Rapptz/discord.py/issues/1249

### lib
- http client
    - requests
- discord client
    - discord.py
- youtube client
    - tbd
- twitch client
    - tbd
- twitter client
    - tbd
- command line tool
    - click

### Hosting
- google app engine

## Kick Start
```
$ git clone https://github.com/chef1234567890/the_bloodhound
$ cd the_bloodhound
$ pip install -r requirements.txt
# set api and secret key
$ vi ./config/secrets.yaml
$ python bloodhound
```
