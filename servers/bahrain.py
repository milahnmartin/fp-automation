from pythonping import ping


class Bahrain:
    Bahrain_url = 'dynamodb.me-south-1.amazonaws.com'

    def ping_server():
        ping_result = ping(target=__class__.Bahrain_url, count=10, timeout=2)

        return {
            'host': __class__.Bahrain_url,
            'avg_latency': ping_result.rtt_avg_ms,
            'min_latency': ping_result.rtt_min_ms,
            'max_latency': ping_result.rtt_max_ms,
            'packet_loss': ping_result.packet_loss
        }
