"""Mass booking routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)


@router.get("/")
async def bookings_home():

    return {
        "message": "Bookings routes working"
    }