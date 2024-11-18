from fastapi import FastAPI
from backend.routers.user_router import user_router

app = FastAPI()

app.include_router(user_router, prefix="/user/{user_id}", tags=["items"])