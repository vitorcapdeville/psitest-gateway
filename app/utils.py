import httpx
from fastapi import HTTPException, Request

async def proxy(request: Request, path: str, service_url: str):
    url = f"{service_url}/{path}"
    async with httpx.AsyncClient(timeout=None) as client:
        headers = dict(request.headers)
        data = None
        if request.method in ["POST", "PUT"]:
            data = await request.body()
        try:
            response = await client.request(request.method, url, data=data, headers=headers, params=request.query_params)
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=str(exc))
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()