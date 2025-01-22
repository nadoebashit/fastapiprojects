from fastapi import FastAPI, Request
from presentation.routes import orders
from presentation.routes.metrics_route import router as metrics_route
from application.services.metrics_service import MetricsService
import time

app = FastAPI()


app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(metrics_route)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()  
    response = await call_next(request) 
    duration = time.time() - start_time  

    
    MetricsService.record_request(request.url.path, request.method, response.status_code)
    MetricsService.record_latency(request.url.path, duration)

    return response

@app.get("/")
def read_root():
    return {"message": "Welcome to the Order Management System"}

