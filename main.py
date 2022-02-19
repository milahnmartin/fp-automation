import dotenv
import requests
import tweepy
from dotenv import load_dotenv, find_dotenv
import os
import time
from logs.discord import Discord
from servers import bahrain
from servers.bahrain import Bahrain

load_dotenv(find_dotenv())
class Monitor_Bahrain:
    # True meaning last ping under 170 ping, a.k.a working
    # False meaning last ping above 200 ping, a.k.a not working
    # differnet for london based server ( digitial ocean )
    bahrain_last = True

    auth = tweepy.OAuth1UserHandler(os.getenv('API_KEY'),os.getenv('API_KEY_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'),os.getenv('ACCESS_TOKEM_SECRET'))
    api = tweepy.API(auth)
    
    def send_tweet(pQuery:str) -> bool:
        __class__.api.update_status(pQuery)
        # Discord.post_webhook(pQuery)
        print('[TWEET WAS SENT]')


    def get_bahrain_status() -> bool:
        print(f'COCK - {__class__.bahrain_last}')
        current_bahrain = Bahrain.ping_server()
        print(f'COCKKKKKKKKKK')
        if __class__.bahrain_last:
            if current_bahrain['min_latency'] > 200:
                __class__.send_tweet('''
                SERVER IS BROKE - bahrain
                                    ''')
                __class__.bahrain_last = False
                __class__.test_logger('Bahrain',current_bahrain['min_latency'])
            else:
                __class__.test_logger('Bahrain',current_bahrain['min_latency'])

        elif not __class__.bahrain_last:

            if current_bahrain['min_latency'] < 200:
                __class__.send_tweet('''
                SERVER IS FIXED AND WORKING - bahrain
                                    ''')
                __class__.bahrain_last = True
                __class__.test_logger('Bahrain',current_bahrain['min_latency'])
            else:
                __class__.test_logger('Bahrain',current_bahrain['min_latency'])

    def test_logger(pServer:str,pResult:dict) -> None:
        print(f'[{pServer} PING WAS CALLED AND RESULT WAS] -> {pResult}ms')
        
        




if __name__ == "__main__":
    while True:
        Monitor_Bahrain.get_bahrain_status()
        time.sleep(5)
        print('TIMER PASSED')
