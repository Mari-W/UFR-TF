from pydantic import BaseSettings


class Env(BaseSettings):
    url: str  # public server url
    secret_key: str  # secret key used to encrypt session
    laurel_metadata_url: str  # open id connect config
    laurel_client_id: str  # oauth client id
    laurel_client_secret: str  # oauth client secret
    laurel_auth_url: str  # logout url with ?redirect= parameter
    discord_bot_token: str  # discord bot secret token
    create_voice_channel_id: str  # the id of the create voice channel channel

    class Config:
        env_file = ".env"


env = Env()
