from fastapi import FastAPI
from httpx import AsyncClient
from loguru import logger

from src.controller import lamp_router

app = FastAPI()
app.include_router(lamp_router)


@app.on_event("startup")
async def connect():
    logger.info("Соединение с сервером")
    try:
        client = AsyncClient()
        url = "http://127.0.0.1:9999"
        await client.get(url)
    except:
        logger.error('Не удалось установить соединение')
