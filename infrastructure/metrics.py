python
import time
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("request_count", "Total request count", ["endpoint", "method", "status"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds", ["endpoint"])

def log_metrics(request, response):
    status = response.status_code
    endpoint = request.url.path
    method = request.method

    REQUEST_COUNT.labels(endpoint=endpoint, method=method, status=status).inc()
    duration = time.time() - request.state.start_time
