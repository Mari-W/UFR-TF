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


# initiate login by redirecting to laurel
async def login(req: Request):
    client = laurel.create_client("laurel")
    return await client.authorize_redirect(env.url + "auth/callback")


# receives the laurel data after login
async def callback(req: Request):
    client = laurel.create_client("laurel")
    token = await client.authorize_access_token(req)
    req.session["laurel"] = token["userinfo"]
    return RedirectResponse(req.url_for("auth_token"))


# logging out by logging out of all laurel services and redirect to login here
async def logout(req: Request):
    req.session.clear()
    return RedirectResponse(
        req,
        "https://auth.laurel.informatik.uni-freiburg.de/auth/logout?redirect="
        + req.url_for("auth_login"),
    )


# stores authorization token in thread shared state for bot to access
async def token(req: Request):
    user = req.session.get("laurel")
    if user is None:
        return RedirectResponse(req.url_for("auth_login"))
    token = str(uuid4())
    state[token] = user

    async def remove_key():
        await asyncio.sleep(5 * 60)
        state.pop(token, None)

    asyncio.create_task(remove_key())
    return templates.TemplateResponse(
        "token.html", {"request": req, "token": token, "sub": user["sub"]}
    )
