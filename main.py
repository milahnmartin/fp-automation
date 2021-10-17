import dotenv
import requests
import tweepy
from dotenv import load_dotenv, find_dotenv
import os
import time
import games
import logs

load_dotenv(find_dotenv())


def auth():
    auth = tweepy.OAuthHandler(
        os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                          os.getenv("ACCESS_TOKEN_SECRET"))

    return auth


def tweet(message: str, game: str):
    auth_status = auth()
    api = tweepy.API(auth_status)
    api.update_status(status=f'#{game}, {message.upper()} @Ultrafyy')
    d = logs.Discord()
    d.post_webhook(f'#{game}, {message.upper()} @Ultrafyy')
    print(f'{game} TWEET SENT')


def monitor_valorant():
    last_ping_status = False
    v_instance = games.Valorant()
    result = v_instance.ping_server()
    print("[GETTING VALORANT PING INFO]")
    time.sleep(1)
    if(result['avg_latency'] < 160 and last_ping_status == False):
        print("Servers are fixed")
        tweet('Bahrain Servers are now working correctly', 'valorant')
        last_ping_status = True
    elif(result['avg_latency'] > 160 and last_ping_status == True):
        print("Servers are fucked")
        tweet('Bahrain Servers are broken', 'valorant')
        last_ping_status = False
    elif(result['avg_latency'] > 160 and last_ping_status == False):
        print("Servers still broken sorry")
    elif(result['avg_latency'] < 160 and last_ping_status == True):
        print("Servers still looking good")


def monitor_fortnite():
    last_ping_status = False
    f_instance = games.Fortnite()
    result = f_instance.ping_server()
    print("[GETTING FORTNITE PING INFO]")
    time.sleep(1)
    if(result['avg_latency'] < 160 and last_ping_status == False):
        print("Servers are fixed")
        tweet('Dubai Servers are now working correctly', 'valorant')
        last_ping_status = True
    elif(result['avg_latency'] > 160 and last_ping_status == True):
        print("Servers are fucked")
        tweet('Dubai Servers are broken', 'valorant')
        last_ping_status = False
    elif(result['avg_latency'] > 160 and last_ping_status == False):
        print("Servers still broken sorry")
    elif(result['avg_latency'] < 160 and last_ping_status == True):
        print("Servers still looking good")


while True:
    monitor_valorant()
