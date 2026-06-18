from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

import os
import logging
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from app.db import init_db, close_db
from app.seed import seed
from app.routes_auth import router as auth_router
from app.routes_bookings import router as bookings_router
from app.routes_payments import router as payments_router, webhook_router
from app.routes_schedule import router as schedule_router
from app.routes_admin import router as admin_router, contact_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s :: %(message)s"
)

logger = logging.getLogger("dolours")

app = FastAPI(
    title="Our Lady of Dolours – Parish Portal API"
)

origins_env = os.environ.get("CORS_ORIGINS", "*")

if origins_env.strip() == "*":
    cors_origins = ["*"]
    allow_credentials = False
else:
    cors_origins = [
        o.strip()
        for o in origins_env.split(",")
        if o.strip()
    ]
    allow_credentials = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

api = APIRouter(prefix="/api")


@api.get("/")
async def root():
    return {
        "app": "Our Lady of Dolours – Parish Portal API",
        "ok": True
    }


@api.get("/health")
async def health():
    return {"ok": True}


api.include_router(auth_router)
api.include_router(bookings_router)
api.include_router(payments_router)
api.include_router(schedule_router)
api.include_router(admin_router)
api.include_router(contact_router)
api.include_router(webhook_router)

app.include_router(api)


@app.on_event("startup")
async def on_startup():
    db = init_db()
    await seed(db)
    logger.info("Startup complete – DB ready, seed applied.")


@app.on_event("shutdown")
async def on_shutdown():
    close_db()