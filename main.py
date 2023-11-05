from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime 

class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    reserved_num: int
    start_date_time: datetime.datetime
    end_date_time: datetime.datetime

class User(BaseModel):
    user_id: int
    username: str=Field(max_length=12)

class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "hello world"}

@app.post("/users")
async def users(users: User):
    return {"users": users}

@app.post("/bookings")
async def bookings(bookings: Booking):
    return {"bookings": bookings}

@app.post("/rooms")
async def rooms(rooms: Room):
    return {"rooms": rooms}

