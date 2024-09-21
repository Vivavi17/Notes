import uvicorn
from fastapi import FastAPI

from src.config import settings
from src.users.router import users_router
from src.notes.router import notes_router

app = FastAPI()

app.include_router(users_router)
app.include_router(notes_router)


@app.get("/ping")
async def ping() -> str:
    return "ok"


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.UVICORN_HOST, port=settings.UVICORN_PORT, reload=True)
