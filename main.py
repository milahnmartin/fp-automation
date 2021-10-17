import dotenv
import requests
import tweepy
from dotenv import load_dotenv, find_dotenv
import os
import time

load_dotenv(find_dotenv())


def auth():
    callback_uri = 'oob'
    auth = tweepy.OAuthHandler(
        os.getenv('API_KEY'), os.getenv('API_SECRET_KEY'), callback_uri)

    if(auth):
        print(True)
    else:
        print(False)


def main():
    print(os.getenv('CONSUMER_KEY'))


if __name__ == "__main__":
    auth()
