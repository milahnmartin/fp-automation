from discord_webhook import DiscordWebhook
import os
from constants import env_var


class Discord:
    webhook_url = env_var['DISCORD_WEBHOOK']

    def post_webhook(message):
        webhook_post = DiscordWebhook(
            url=__class__.webhook_url, rate_limit_retry=True, content=message)
        response = webhook_post.execute()
        print(f'[FP-DISCORD -> MESSAGE SENT]')
