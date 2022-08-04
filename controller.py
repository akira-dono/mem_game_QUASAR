from sql import SQL_REQUESTS;
from db import mycursor, mydb;

def createUser(name, device_id):
    mycursor.execute(SQL_REQUESTS["INSERT_USER"], (name, device_id));
    mydb.commit();

def getUsers():
    mycursor.execute(SQL_REQUESTS["GET_USERS"]);
    user = mycursor.fetchall();
    user_array = [];
    for i in range(len(user)):
        user_object = {
            "ID": user[i][0],
            "NICKNAME": user[i][1],
            "DEVICE_ID": user[i][2]
        };
        user_array.append(user_object);
    return user_array

def getUser(id):
    mycursor.execute(SQL_REQUESTS["GET_USER"]+id);
    ids = mycursor.fetchone();
    user = {
        "ID": ids[0],
        "NICKNAME": ids[1],
        "DEVICE_ID": ids[2]
    };
    return user;

def createRoom(player_counter, room_name, private, pas, room_active):
    if private:
        vals = (player_counter, room_name, private, pas, room_active);
        mycursor.execute(SQL_REQUESTS["INSERT_ROOM"], vals);
        mydb.commit();

    elif not(private):
        pas = 0;
        vals = (player_counter, room_name, private, pas, room_active);
        mycursor.execute(SQL_REQUESTS["INSERT_ROOM"], vals);
        mydb.commit();

def getRoom():
    mycursor.execute(SQL_REQUESTS["GET_ROOMS"]);