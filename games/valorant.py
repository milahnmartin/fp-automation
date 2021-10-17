import time
import os
from pythonping import ping
last_ping_status = False


class Valorant:
    def __init__(self) -> None:
        self.url = '157.175.10.11'

    def ping_server(self):
        ping_result = ping(target=self.url, count=10, timeout=2)

        return {
            'host': self.url,
            'avg_latency': ping_result.rtt_avg_ms,
            'min_latency': ping_result.rtt_min_ms,
            'max_latency': ping_result.rtt_max_ms,
            'packet_loss': ping_result.packet_loss
        }



