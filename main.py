import dotenv
import requests
import tweepy
from dotenv import load_dotenv, find_dotenv
import os
import time
import games
import logs

load_dotenv(find_dotenv())

# GLOBAL VARIABLES
valorant_last_status = True
fortnite_last_status = False


def tweet(message: str, game: str, last_status: bool):
    global valorant_last_status
    global fortnite_last_status
    if(game == 'valorant'):
        if(valorant_last_status):
            game_last_state = 1
        else:
            game_last_state = 0
    elif(game == 'fortnite'):
        if(fortnite_last_status):
            game_last_state = 1
        else:
            game_last_state = 0

    auth = tweepy.OAuthHandler(
        os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                          os.getenv("ACCESS_TOKEN_SECRET"))
    print("[TWEEPY AUTH -> SUCCESS]")
    api = tweepy.API(auth)
    if(not last_status):
        api.update_status_with_media(
            'https://play-lh.googleusercontent.com/x3XxTcEYG6hYRZwnWAUfMavRfNNBl8OZweUgZDf2jUJ3qjg2p91Y8MudeXumaQLily0', f'''#{game.upper()} 
    
    ❌❌ UHM, SOMETHING IS WRONG WITH THE SERVERS ATM !! ❌❌


        ''')
        discord_i = logs.Discord()
        discord_i.post_webhook(
            f'[TWEET WAS SENT -> ❌❌ UHM, SOMETHING IS WRONG WITH THE SERVERS ATM !! ❌❌]')
        # api.update_status(status=)
    else:
        api.update_status_with_media('https://play-lh.googleusercontent.com/x3XxTcEYG6hYRZwnWAUfMavRfNNBl8OZweUgZDf2jUJ3qjg2p91Y8MudeXumaQLily0',
                                     '✅✅ GOODNEWS ! SERVERS ARE PERFORMING NORMALLY !! ✅✅')
        discord_i = logs.Discord()
        discord_i.post_webhook(
            f'[TWEET WAS SENT -> ✅✅ HEY YOU READING THIS ! THE SERVERS ARE UP AND WORKING !! ✅✅]')
    #     api.update_status(status=f'''#{game.upper()}

    # ✅✅ GOODNEWS ! SERVERS ARE PERFORMING NORMALLY !! ✅✅

    #     ''')

        db_instance = logs.Db()
        db_instance.query(game, message, game_last_state)
        print(f'[{game.upper()} -> TWEET SENT]')


def monitor_valorant():
    global valorant_last_status
    v_instance = games.Valorant()
    result = v_instance.ping_server()
    print("[GETTING VALORANT PING INFO]")
    time.sleep(5)
    if(result['avg_latency'] < 160 and valorant_last_status == False):
        print("[VALORANT BAHRAIN - FIXED] ->", result['avg_latency'])
        tweet('Bahrain Servers are now working correctly', 'valorant', True)
        valorant_last_status = True
    elif(result['avg_latency'] > 160 and valorant_last_status == True):
        print("[VALORANT BAHRAIN - BROKEN] ->", result['avg_latency'])
        tweet('Bahrain Servers are broken', 'valorant', False)
        valorant_last_status = False
    elif(result['avg_latency'] > 160 and valorant_last_status == False):
        print("[VALORANT BAHRAIN - STILL BROKEN] ->", result['avg_latency'])
    elif(result['avg_latency'] < 160 and valorant_last_status == True):
        print("[VALORANT BAHRAIN - STILL WORKING NORMALLY] ->",
              result['avg_latency'])


def monitor_fortnite():
    global fortnite_last_status
    f_instance = games.Fortnite()
    result = f_instance.ping_server()
    print("[GETTING FORTNITE PING INFO]")
    time.sleep(5)
    if(result['avg_latency'] < 160 and fortnite_last_status == False):
        print("[FORTNITE BAHRAIN - FIXED] ->", result['avg_latency'])
        tweet('Bahrain Servers are now working correctly', 'fortnite', True)
        fortnite_last_status = True
    elif(result['avg_latency'] > 160 and fortnite_last_status == True):
        print("[VALORANT BAHRAIN - BROKEN] ->", result['avg_latency'])
        tweet('Bahrain Servers are broken', 'fortnite', False)
        fortnite_last_status = False
    elif(result['avg_latency'] > 160 and fortnite_last_status == False):
        print("[FORTNITE BAHRAIN - STILL BROKEN] ->", result['avg_latency'])
    elif(result['avg_latency'] < 160 and fortnite_last_status == True):
        print("[FORTNITE BAHRAIN - STILL WORKING NORMALLY] ->",
              result['avg_latency'])


if __name__ == '__main__':
    while True:
        monitor_valorant()
        monitor_fortnite()
