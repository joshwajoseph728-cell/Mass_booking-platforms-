"""Mass schedule routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/schedule",
    tags=["schedule"]
)


@router.get("/")
async def schedule_home():

    return {
        "message": "Schedule routes working"
    }