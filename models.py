from pydantic import BaseModel

class User(BaseModel):
    name: str
    device_id: int

