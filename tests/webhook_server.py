from fastapi import FastAPI, Request
import logging

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/webhooks")
async def print_webhook_data_GET(request: Request):
    body = await request.body()
    logger.error("received from HTTP GET method")
    logger.error(body)


@app.post("/webhooks")
async def print_webhook_data_POST(request: Request):
    body = await request.body()
    logger.error("received from HTTP POST method")
    logger.error(body)
