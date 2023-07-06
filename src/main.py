import asyncio

from dotenv import load_dotenv
from fastapi import FastAPI as Api, Request
from starlette.middleware.sessions import SessionMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from .auth import login, logout, token, callback
from .bot import Bot
from .env import env

## FastAPI ##############################################################################

app = Api()

# Limiter & Middleware


limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(SessionMiddleware, secret_key=env.secret_key, max_age=94608000)

# Events


@app.on_event("startup")
async def startup():
    load_dotenv()
    asyncio.create_task(bot.start(env.discord_bot_token))


# Routes


@app.get("/auth/login")
async def auth_login(request: Request):
    return await login(request)


@app.get("/auth/logout")
async def auth_logout(request: Request):
    return await logout(request)


@app.get("/token")
# maximum of 1 token every six second
@limiter.limit("10/minute")
async def auth_token(request: Request):
    return await token(request)


@app.get("/auth/callback")
async def auth_callback(request: Request):
    return await callback(request)


## Discord Bot ##########################################################################

bot = Bot()

# Events


@bot.event
async def on_voice_state_update(member, before, after):
    await bot.voice(member, before, after)
