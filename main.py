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


def tweet(message: str, game: str):
    auth = tweepy.OAuthHandler(
        os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                          os.getenv("ACCESS_TOKEN_SECRET"))
    print("[TWEEPY AUTH -> SUCCESS]")
    api = tweepy.API(auth)
    api.update_status(status=f'#{game} -> {message.upper()} @Ultrafyy')
    d = logs.Discord()
    print(f'[{game.upper()} -> TWEET SENT]')


def monitor_valorant():
    global valorant_last_status
    v_instance = games.Valorant()
    result = v_instance.ping_server()
    print("[GETTING VALORANT PING INFO]")
    time.sleep(5)
    if(result['avg_latency'] < 160 and valorant_last_status == False):
        print("[VALORANT BAHRAIN - FIXED]")
        tweet('Bahrain Servers are now working correctly', 'valorant')
        valorant_last_status = True
    elif(result['avg_latency'] > 160 and valorant_last_status == True):
        print("[VALORANT BAHRAIN - BROKEN]")
        tweet('Bahrain Servers are broken', 'valorant')
        valorant_last_status = False
    elif(result['avg_latency'] > 160 and valorant_last_status == False):
        print("[VALORANT BAHRAIN - STILL BROKEN]")
    elif(result['avg_latency'] < 160 and valorant_last_status == True):
        print("[VALORANT BAHRAIN - STILL WORKING NORMALLY]")


def monitor_fortnite():
    global fortnite_last_status
    f_instance = games.Fortnite()
    result = f_instance.ping_server()
    print("[GETTING FORTNITE PING INFO]")
    time.sleep(5)
    if(result['avg_latency'] < 160 and fortnite_last_status == False):
        print("Servers are fixed")
        tweet('Dubai Servers are now working correctly', 'valorant')
        fortnite_last_status = True
    elif(result['avg_latency'] > 160 and fortnite_last_status == True):
        print("Servers are fucked")
        tweet('Dubai Servers are broken', 'valorant')
        fortnite_last_status = False
    elif(result['avg_latency'] > 160 and fortnite_last_status == False):
        print("Servers still broken sorry")
    elif(result['avg_latency'] < 160 and fortnite_last_status == True):
        print("Servers still looking good")


while True:
    monitor_valorant()
