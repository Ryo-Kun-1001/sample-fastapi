from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

DATABASE_URL = settings.TEST_DATABASE_URL if settings.TESTING else settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    get_db はセッションを確立
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
