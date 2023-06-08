# bot.py
import asyncio
from uuid import uuid4

from dotenv import load_dotenv
from fastapi import FastAPI as Api, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware

from .bot import Bot
from .env import env
from .state import state

api = Api()
bot = Bot()


api.add_middleware(
  SessionMiddleware, secret_key=env.secret_key, max_age=94608000)


@api.on_event("startup")
async def startup():
  load_dotenv()
  asyncio.create_task(bot.start(env.discord_bot_token))


laurel = OAuth()
laurel.register(
  "laurel",
  server_metadata_url=env.laurel_metadata_url,
  client_id=env.laurel_client_id,
  client_secret=env.laurel_client_secret,
  client_kwargs={"scope": "openid profile studies"},
)

@api.get("/auth/login")
async def auth_login(req: Request):
  client = laurel.create_client("laurel")
  return await client.authorize_redirect(req, env.url + "auth/callback")

@api.get("/auth/logout")
async def logout(req: Request):
  req.session.clear()
  return RedirectResponse(req.url_for("auth_login"))

@api.get("/auth/token")
async def auth_token(req: Request):
  session = req.session["laurel"]
  if session is None:
    RedirectResponse(req.url_for("auth_login"))
  token = str(uuid4())
  state[token] = req.session["laurel"]
  return {"account": "https://auth.laurel.informatik.uni-freiburg.de", "token": token}
https://6bd15c7d-f7e1-4971-a235-15fde9e9f0a3.fr.bw-cloud-instance.org/auth/callback
http://6bd15c7d-f7e1-4971-a235-15fde9e9f0a3.fr.bw-cloud-instance.org/auth/callback
@api.get("/auth/callback")
async def auth_callback(req: Request):
  client = laurel.create_client("laurel")
  token = await client.authorize_access_token(req)
  req.session["laurel"] = token["userinfo"]
  return RedirectResponse(req.url_for("auth_token"))
