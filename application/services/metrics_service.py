from prometheus_client import Counter, Histogram

class MetricsService:
    REQUEST_COUNT = Counter("request_count", "Total request count", ["endpoint", "method", "status"])
    REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds", ["endpoint"])

    @classmethod
    def record_request(cls, endpoint: str, method: str, status: int):
        cls.REQUEST_COUNT.labels(endpoint=endpoint, method=method, status=status).inc()

    @classmethod
    def record_latency(cls, endpoint: str, duration: float):
        cls.REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)