from pythonping import ping


class Bahrain2:
    bahrain_url = '157.175.10.11'

    def ping_server() -> dict:
        ping_result = ping(target=__class__.url, count=10, timeout=2)

        return {
            'host': __class__.url,
            'avg_latency': ping_result.rtt_avg_ms,
            'min_latency': ping_result.rtt_min_ms,
            'max_latency': ping_result.rtt_max_ms,
            'packet_loss': ping_result.packet_loss
        }



