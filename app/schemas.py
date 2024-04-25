"""
このファイルではFastAPI (pydantic) を用いたデータ構造を定義
"""

import datetime
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    """
    UserCreate はユーザー登録APIのリクエストJSONを受け取るためのスキーマ
    """
    user_name: str = Field(max_length=12)


class User(UserCreate):
    """
    User はユーザー情報の持ち回しのためのスキーマ
    """
    user_id: int

    class Config:
        orm_mode: True


class RoomCreate(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int


class Room(RoomCreate):
    room_id: int

    class Config:
        orm_mode: True


class BookingCreate(BaseModel):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime


class Booking(BookingCreate):
    booking_id: int

    class Config:
        orm_mode: True
