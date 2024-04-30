import pytest  # type: ignore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base, get_db_url
from api import cruds

# テスト用のデータベースURL
DATABASE_URL = get_db_url()

# テスト用のデータベースエンジン
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# テーブルを作成
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """テスト用のデータベースセッションを生成するフィクスチャ"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_get_users(db_session):
    """ユーザーを取得するテスト関数"""
    users = cruds.get_users(db=db_session)
    print(users)
    assert isinstance(users, list)
