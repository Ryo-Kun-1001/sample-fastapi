from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
import logging
import time

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db_url():
    """設定からデータベースのURLを取得する。"""
    from .config import settings  # 設定の遅延読み込み
    return settings.TEST_DATABASE_URL if settings.TESTING else settings.DATABASE_URL


def create_db_engine(url, max_attempts=10, delay=2):
    """データベースエンジンを生成し、必要に応じてリトライを行う。"""
    attempt_count = 0
    while attempt_count < max_attempts:
        try:
            engine = create_engine(url)
            # 接続テストを行う
            conn = engine.connect()
            conn.close()
            return engine
        except SQLAlchemyError as e:
            attempt_count += 1
            logger.warning(f"データベース接続に失敗しました。 {attempt_count} 回目の試行: {e}")
            if attempt_count >= max_attempts:
                logger.error("データベース接続に最終的に失敗しました。")
                raise
            time.sleep(delay)  # 次のリトライまで少し待つ


def get_engine():
    """データベースエンジンを取得する。"""
    url = get_db_url()
    return create_db_engine(url)


# グローバル変数としてengineを生成
engine = create_db_engine(get_db_url())

# SQLAlchemyのセッションファクトリを作成
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=get_engine())

# データベースモデルのベースクラス
Base = declarative_base()


def get_db():
    """データベースセッションを提供するジェネレータ。"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
