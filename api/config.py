from pydantic_settings import BaseSettings  # type: ignore
from typing import Dict


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+mysqlconnector://user:password@db:3306/mydatabase"
    TEST_DATABASE_URL: str = "mysql+mysqlconnector://user:password@test_db:3307/test_db"

    # テスト実行時にTrueにする
    TESTING: bool = False

    class Config:
        config_dict: Dict[str, str] = {
            "env_file": ".env",
            # 必要に応じて他の設定もここに追加可能
        }


# Settingsインスタンスの作成
settings = Settings()
