import dotenv
import requests
import tweepy
from dotenv import load_dotenv, find_dotenv
import os
import time

load_dotenv(find_dotenv())


def auth():
    auth = tweepy.OAuthHandler(
        os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                          os.getenv("ACCESS_TOKEN_SECRET"))

    return auth


def tweet():
    auth_status = auth()
    api = tweepy.API(auth_status)
    api.update_status(status="Fingerprint Automation Test")
    print("TWEET SUCCESS")


if __name__ == "__main__":
    tweet()
