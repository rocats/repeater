from pydantic import BaseModel


class AppConfig(BaseModel):
    debug: bool
    env: str
    log_level: str
