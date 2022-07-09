from fastapi import FastAPI
from models import *;
from controller import *;

app = FastAPI()

@app.post('/user/', response_model=User)
async def create_user(user: User):
    name = user.name;
    device_id = user.device_id;
    createUser(name, device_id);
    return user;

@app.get('/user/')
async def get_users():
    return getUsers();
