import dotenv
import requests
import tweepy
from dotenv import load_dotenv, find_dotenv
import os
import time
import games

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
    print(f'{game} TWEET SENT')


while True:
    p = games.Valorant()
    result = p.ping_server()
    print(result)
    time.sleep(2)
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
