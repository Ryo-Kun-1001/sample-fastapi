from pydantic_settings import BaseSettings  # type: ignore
from pydantic import ConfigDict


class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_ROOT_PASSWORD: str
    TEST_DATABASE: str
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    TESTING: bool = False  # テスト実行時にTrueにする

    class Config(ConfigDict):
        env_file = ".env"


# Settingsインスタンスの作成
settings = Settings()
