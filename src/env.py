from pydantic import BaseSettings


class Env(BaseSettings):
  url: str
  secret_key: str
  laurel_metadata_url: str
  laurel_client_id: str
  laurel_client_secret: str
  discord_bot_token: str
  discord_auth_channel: str


  class Config:
    env_file = ".env"


env = Env()
