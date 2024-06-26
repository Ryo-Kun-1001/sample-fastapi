from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from api import domains, models, schemas
from .database import get_db, engine

# DBの作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://frontend:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Success"}


@app.get("/users", response_model=List[schemas.User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return domains.get_users(db, skip, limit)


@app.post("/users", response_model=List[schemas.User])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return domains.create_user(db=db, user=user)


@app.get("/rooms", response_model=List[schemas.Room])
async def get_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return domains.get_rooms(db, skip, limit)


@app.post("/rooms", response_model=List[schemas.Room])
async def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return domains.create_room(db=db, room=room)


@app.get("/bookings", response_model=List[schemas.Booking])
async def get_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return domains.get_bookings(db, skip, limit)


@app.post("/bookings", response_model=List[schemas.Booking])
async def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return domains.create_booking(db=db, booking=booking)
