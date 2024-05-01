import pytest  # type: ignore
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from api.database import get_db_url, Base
from api.models import Booking, Room, User


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(get_db_url())
    Base.metadata.create_all(engine)  # テーブルの作成
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    yield session  # ここでテストが実行される
    session.close()
    Base.metadata.drop_all(engine)  # テスト後、テーブルを削除


@pytest.fixture(scope="function")
def db_with_data(db_session):
    # Users
    users = [
        User(user_id=1, user_name='ぽん'),
        User(user_id=2, user_name='ささかわ'),
        User(user_id=3, user_name='くらた'),
        User(user_id=4, user_name='ふじた')
    ]
    db_session.add_all(users)
    db_session.commit()

    # Rooms
    rooms = [
        Room(room_id=1, room_name='Bear', capacity=4),
        Room(room_id=2, room_name='Bull', capacity=8),
        Room(room_id=3, room_name='Hog', capacity=6)
    ]
    db_session.add_all(rooms)
    db_session.commit()

    # Bookings
    bookings = [
        Booking(booking_id=1, user_id=1, room_id=1, booked_num=2, start_datetime=datetime(
            2024, 4, 1, 9, 0), end_datetime=datetime(2024, 4, 1, 10, 0)),
        Booking(booking_id=2, user_id=1, room_id=2, booked_num=3, start_datetime=datetime(
            2024, 4, 1, 10, 0), end_datetime=datetime(2024, 4, 1, 11, 0)),
        Booking(booking_id=3, user_id=2, room_id=3, booked_num=6, start_datetime=datetime(
            2024, 4, 1, 9, 0), end_datetime=datetime(2024, 4, 1, 10, 0)),
        Booking(booking_id=4, user_id=3, room_id=2, booked_num=3, start_datetime=datetime(
            2024, 4, 1, 9, 0), end_datetime=datetime(2024, 4, 1, 10, 0))
    ]
    db_session.add_all(bookings)
    db_session.commit()
    yield db_session
