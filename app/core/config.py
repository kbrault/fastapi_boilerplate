from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Boilerplate"
    debug: bool = True

settings = Settings()
