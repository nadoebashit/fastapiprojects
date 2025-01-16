from fastapi import APIRouter
from application.services.metrics_service import MetricsService

router = APIRouter()

@router.get("/metrics")
async def get_metrics():
    # Получаем текущее значение счетчика
    request_count = MetricsService.REQUEST_COUNT.collect()[0].samples
    request_count_value = sum(sample.value for sample in request_count)

    return {
        "request_count": request_count_value,
        "request_latency": MetricsService.REQUEST_LATENCY.collect()
    }