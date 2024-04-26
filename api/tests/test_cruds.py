import pytest  # type: ignore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base  # モデルのBaseを適切にインポートしてください
from api import cruds


@pytest.fixture(scope="module")
def db_session():
    # テスト用データベースの接続設定
    engine = create_engine('sqlite:///:memory:')  # または他のテスト用DB接続文字列
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()


def test_get_users(db_session):
    users = cruds.get_users(db_session)
    assert isinstance(users, list)
