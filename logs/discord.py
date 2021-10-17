from discord_webhook import DiscordWebhook
import os


class Discord:
    def __init__(self) -> None:
        self.webhook_url = os.getenv('DISCORD_WEBHOOK')

    def post_webhook(self, message):
        webhook_post = DiscordWebhook(
            url=self.webhook_url, rate_limit_retry=True, content=message)
        response = webhook_post.execute()
        print(f'Discord Message {message} has been sent')
