from fastapi import FastAPI, Request, Depends
from typing import Annotated
from app.settings import get_settings, Settings
from app.utils import proxy

app = FastAPI()


@app.post("/login", tags=["auth"])
async def login(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "login", settings.PSITEST_AUTH)


@app.post("/signup", tags=["cadastro"])
async def signup(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    print(settings.PSITEST_CADASTRO)
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


@app.post("/validate-reset-password-code", tags=["auth"])
async def validate_reset_password_code(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "validate-reset-password-code", settings.PSITEST_AUTH)


@app.put("/reset-password", tags=["auth"])
async def reset_password(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "reset-password", settings.PSITEST_AUTH)


@app.get("/users/me", tags=["cadastro"])
async def get_user_details(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "users/me", settings.PSITEST_CADASTRO)


@app.post("/questionarios", tags=["questionarios"])
async def buscar_questioanrios(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "questionarios", settings.PSITEST_QUESTIONARIOS)


@app.get("/respostas", tags=["respostas"])
async def buscar_questionarios_enviados_por_psicologo(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "respostas", settings.PSITEST_RESPOSTAS)


@app.get("/respostas/{envio_id}", tags=["respostas"])
async def buscar_respostas_por_envio(
    request: Request,
    envio_id: int,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, f"respostas/{envio_id}", settings.PSITEST_RESPOSTAS)


@app.post("/envio", tags=["respostas"])
async def enviar_questionario(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "envio", settings.PSITEST_RESPOSTAS)


@app.get("/envios", tags=["respostas"])
async def buscar_envios_por_email(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "envios", settings.PSITEST_RESPOSTAS)


@app.post("/responder", tags=["respostas"])
async def responder_questionario(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
):
    return await proxy(request, "responder", settings.PSITEST_RESPOSTAS)
