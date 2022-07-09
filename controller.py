from sql import SQL_REQUESTS;
from db import mycursor, mydb;

def createUser(name, device_id):
    mycursor.execute(SQL_REQUESTS["INSERT_USER"], (name, device_id));
    mydb.commit();

def getUsers():
    mycursor.execute(SQL_REQUESTS["GET_USERS"]);
    ids = mycursor.fetchall();
    return ids