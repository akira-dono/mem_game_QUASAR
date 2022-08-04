from fastapi import FastAPI
from models import *;
from controller import *;

app = FastAPI()



#! PUT запрос лучше
@app.post('/user/', response_model=User)
async def create_user(user: User):
    name = user.name;
    device_id = user.device_id;
    createUser(name, device_id);
    return user;

@app.get('/user/')
async def get_users():
    return getUsers();

@app.post('/user/{user_id}')
async def user(user_id: str):
    return getUser(user_id);

@app.post('/room/', response_model=Room)
async def create_room(room: Room):
    ...