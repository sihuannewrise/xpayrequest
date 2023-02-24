from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Заявки на оплату'
    app_description: str = 'Передача заявок в оплату'

    database_url: str

    ydb_endpoint: str
    ydb_database: str

    class Config:
        env_file = 'ENV/.env'

settings = Settings()
