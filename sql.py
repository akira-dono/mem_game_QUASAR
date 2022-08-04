SQL_REQUESTS = {
    "INSERT_USER": "INSERT INTO users (nickname, device_id) VALUES (%s, %s)",
    "GET_USERS": "SELECT * FROM users",
    "GET_USER": "SELECT * FROM users WHERE id = ",
    "INSERT_ROOM": "INSERT INTO room (player_counter, room_name, private, pas, room_active) VALUES (%s, %s, %s, %s, %s)"
}
