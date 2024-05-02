from sqlalchemy.orm import Session
from . import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    get_users はユーザー一覧取得
    """
    return db.query(models.User).order_by(models.User.user_id).offset(skip).limit(limit).all()


def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    """
    get_rooms は会議室一覧取得
    """
    return db.query(models.Room).offset(skip).limit(limit).all()


def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    """
    get_users は予約一覧取得
    """
    return db.query(models.Booking).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User) -> models.User:
    """
    create_user はユーザー登録
    """
    db_user = models.User(user_name=user.user_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # インスタンスをリフレッシュ
    return db_user


def create_room(db: Session, room: schemas.Room) -> models.Room:
    """
    create_room は会議室登録
    """
    db_room = models.Room(room_name=room.room_name, capacity=room.capacity)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)  # インスタンスをリフレッシュ
    return db_room


def create_booking(db: Session, booking: schemas.Booking) -> models.Booking:
    """
    create_booking は予約登録
    """
    db_booking = models.Booking(
        user_id=booking.user_id,
        room_id=booking.room_id,
        booked_num=booking.booked_num,
        start_datetime=booking.start_datetime,
        end_datetime=booking.end_datetime,
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)  # インスタンスをリフレッシュ
    return db_booking
