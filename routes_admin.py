"""Admin routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

contact_router = APIRouter(
    prefix="/contact",
    tags=["contact"]
)


@router.get("/")
async def admin_home():

    return {
        "message": "Admin routes working"
    }


@contact_router.get("/")
async def contact_home():

    return {
        "message": "Contact routes working"
    }