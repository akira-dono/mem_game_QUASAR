from pydantic import BaseModel

class User(BaseModel):
    name: str
    device_id: int

class Room(BaseModel):
    player_counter: int
    room_name: str
    private: bool
    pas: int
    room_active: bool