from . import cruds, schemas
from sqlalchemy.orm import Session


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return cruds.get_users(db, skip, limit)


def create_user(db: Session, user: schemas.User):
    cruds.create_user(db=db, user=user)
    return cruds.get_users(db=db, skip=0, limit=100)


def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return cruds.get_rooms(db, skip, limit)


def create_room(db: Session,  room: schemas.Room):
    cruds.create_room(db=db, room=room)
    return cruds.get_rooms(db=db, skip=0, limit=100)


def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return cruds.get_bookings(db, skip, limit)


def create_booking(db: Session,  booking: schemas.Booking):
    cruds.create_booking(db=db, booking=booking)
    return cruds.get_bookings(db=db, skip=0, limit=100)
