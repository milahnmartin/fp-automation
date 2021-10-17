import dotenv
import requests
import tweepy
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def auth():
    pass


def main():
    print(os.getenv('CONSUMER_KEY'))


if __name__ == "__main__":
    main()
