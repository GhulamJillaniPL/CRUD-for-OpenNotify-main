from pydantic import BaseSettings

class Settings(BaseSettings):
    open_notify_url: str = "http://api.open-notify.org"
    api_title: str = "ISS Tracking API"
    api_version: str = "v1"

    class Config:
        env_file = ".env"

settings = Settings()