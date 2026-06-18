"""Auth routes: register, login, me, logout."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.get("/")
async def auth_home():

    return {
        "message": "Auth routes working"
    }