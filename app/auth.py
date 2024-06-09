import httpx
from fastapi import APIRouter, Request

from app.settings import get_settings

router = APIRouter()


async def proxy(request: Request, path: str):
    url = f"{get_settings().PSITEST_AUTH}/{path}"
    async with httpx.AsyncClient() as client:
        if request.method == "GET":
            response = await client.get(url, params=request.query_params)
        elif request.method == "POST":
            data = await request.body()
            headers = dict(request.headers)
            response = await client.post(url, data=data, headers=headers)
        elif request.method == "PUT":
            data = await request.body()
            headers = dict(request.headers)
            response = await client.put(url, data=data, headers=headers, params=request.query_params)
    return response.json()


@router.post("/login/", tags=["auth"])
async def login(request: Request):
    return await proxy(request, "token")


@router.post("/signup/", tags=["auth"])
async def signup(request: Request):
    return await proxy(request, "signup")


@router.put("/verify-email", tags=["auth"])
async def verify_email(request: Request):
    return await proxy(request, "verify-email")


@router.put("/forgot-password", tags=["auth"])
async def forgot_password(request: Request):
    return await proxy(request, "forgot-password")


@router.put("/reset-password", tags=["auth"])
async def reset_password(request: Request):
    return await proxy(request, "reset-password")
