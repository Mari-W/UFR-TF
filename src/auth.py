import asyncio
from uuid import uuid4
from authlib.integrations.starlette_client import OAuth
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .env import env
from .bot import state

# openid connect client for laurel
laurel = OAuth()
laurel.register(
    "laurel",
    server_metadata_url=env.laurel_metadata_url,
    client_id=env.laurel_client_id,
    client_secret=env.laurel_client_secret,
    client_kwargs={"scope": "openid profile studies"},
)

# jinja html templates
templates = Jinja2Templates(directory="templates")


async def login(request: Request):
    client = laurel.create_client("laurel")
    # initiate login by redirecting to laurel
    return await client.authorize_redirect(env.url + "auth/callback")


async def callback(request: Request):
    client = laurel.create_client("laurel")
    # receives the laurel data after login
    token = await client.authorize_access_token(request)
    request.session["laurel"] = token["userinfo"]
    return RedirectResponse(request.url_for("auth_token"))


async def logout(request: Request):
    # logout locally
    request.session.clear()
    # logging out by logging out of all laurel services and redirect to login here
    return RedirectResponse(
        request,
        "https://auth.laurel.informatik.uni-freiburg.de/auth/logout?redirect="
        + str(request.url_for("auth_login")),
    )


async def token(request: Request):
    user = request.session.get("laurel")
    if user is None:
        return RedirectResponse(request.url_for("auth_login"))
    token = str(uuid4())

    # stores authorization token along user information in thread shared state for bot to access
    state[token] = user

    # key is valid for 5 minutes
    async def remove_key():
        await asyncio.sleep(5 * 60)
        state.pop(token, None)

    asyncio.create_task(remove_key())
    return templates.TemplateResponse(
        "token.html", {"request": request, "token": token, "sub": user["sub"]}
    )
