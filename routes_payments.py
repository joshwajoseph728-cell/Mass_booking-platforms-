"""Payments routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

webhook_router = APIRouter(
    tags=["payments"]
)


@router.get("/")
async def payments_home():

    return {
        "message": "Payments routes working"
    }


@webhook_router.get("/webhook/stripe")
async def stripe_webhook():

    return {
        "ok": True
    }