from fastapi import FastAPI, Request, Depends
from typing import Annotated
from app.settings import get_settings, Settings
from app.utils import proxy

app = FastAPI()

SERVICE_URL = get_settings().PSITEST_AUTH


@app.post("/login", tags=["auth"])
async def login(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "login", settings.PSITEST_AUTH)


@app.post("/signup", tags=["auth"])
async def signup(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "signup", settings.PSITEST_CADASTRO)


@app.put("/verify-email", tags=["auth"])
async def verify_email(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "verify-email", settings.PSITEST_AUTH)


@app.put("/forgot-password", tags=["auth"])
async def forgot_password(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "forgot-password", settings.PSITEST_AUTH)


@app.put("/reset-password", tags=["auth"])
async def reset_password(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "reset-password", settings.PSITEST_AUTH)
