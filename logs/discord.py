from discord_webhook import DiscordWebhook
import os


class Discord:
    webhook_url = os.getenv('DISCORD_WEBHOOK')

    def post_webhook(message):
        webhook_post = DiscordWebhook(
            url=__class__.webhook_url, rate_limit_retry=True, content=message)
        response = webhook_post.execute()
        print(f'[FP-DISCORD -> MESSAGE SENT]')
