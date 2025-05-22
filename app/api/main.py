from fastapi import FastAPI

from app.api.v1 import health
from app.infra.db.conn import close, connect

app = FastAPI(debug=True)

app.include_router(health.router, prefix="/api/v1", tags=["health"])


@app.on_event("startup")
async def startup():
    await connect()


@app.on_event("shutdown")
async def shutdown():
    await close()
