from fastapi import APIRouter

from aiohttp import ClientSession

from server.models.collections import User

from server.models.config import env

app = APIRouter(prefix="/auth", tags=["auth"])


@app.get("/{token}")

async def authorize(token: str):
    """

    Temporary endpoint to authorize users
    """

    async with ClientSession() as session:

        async with session.get(

            f"https://{env.AUTH0_DOMAIN}/userinfo",

            headers={"Authorization": f"Bearer {token}"},
        ) as response:

            user = User(**await response.json())
            
            print(user)
            
            return await user.create()    
        