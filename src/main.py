import uvicorn
from fastapi import FastAPI

from src.config import settings

app = FastAPI()


@app.get("/ping")
async def ping() -> str:
    return "ok"


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.UVICORN_HOST, port=settings.UVICORN_PORT, reload=True)
