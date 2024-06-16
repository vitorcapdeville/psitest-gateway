import httpx
from fastapi import HTTPException, Request


async def proxy(request: Request, path: str, service_url: str):
    url = f"{service_url}/{path}"
    async with httpx.AsyncClient() as client:
        if request.method == "GET":
            response = await client.get(url, params=request.query_params)
        elif request.method == "POST":
            data = await request.body()
            headers = dict(request.headers)
            response = await client.post(url, data=data, headers=headers, params=request.query_params)
        elif request.method == "PUT":
            data = await request.body()
            headers = dict(request.headers)
            response = await client.put(url, data=data, headers=headers, params=request.query_params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()
