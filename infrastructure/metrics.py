from prometheus_client import Counter

request_count = Counter("api_requests_total", "Total API requests", ["method", "endpoint", "status"])

@app.middleware("http")
async def track_requests(request, call_next):
    response = await call_next(request)
    request_count.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code,
    ).inc()
    return response
