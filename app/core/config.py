from typing import Optional
from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Payment requests forwarding'
    app_description: str = 'Payment requests forwarding application'

    database_url: str
    secret: str = 'SECRET'
    # sqlalchemy_database_pem: str

    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    dd_token: str
    dd_secret: str

    class Config:
        env_file = 'infra/ENV/.env'


settings = Settings()
