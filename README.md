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

## env
### lang
```
the_bloodhound$ pyenv version
3.6.8 (set by /Users/bloodhound/.pyenv/version)
```
- Why not use python 3.7
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

### Class design
```
the_bloodhound
├─ HttpClient
├─ Discord
├─ Stream
|  ├─ Youtube
|  └─ Twitch
└─ Twitter
```

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