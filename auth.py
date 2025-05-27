VALID_USERS = {
    "alice": "password123",
    "bob": "securepass",
    "admin": "adminpass"
}


def get_user(username):
    if username.lower() not in VALID_USERS:
        raise KeyError("User does not exist")
    return VALID_USERS[username.lower()]

def is_valid_user(username):
    username = username.lower()
    return username in VALID_USERS

def authenticate(username, password):
    username = username.lower()
    if not is_valid_user(username):
        return "User not found"
    if VALID_USERS[username] != password:
        return "Incorrect password"
    return "Login successful"

def change_password(username, old_password, new_password):
    username = username.lower()
    if not is_valid_user(username):
        return "User not found"
    if VALID_USERS[username] != old_password:
        return "Incorrect old password"
    if not new_password:
        return "New password cannot be empty"
    VALID_USERS[username] = new_password
    return "Password changed successfully"
