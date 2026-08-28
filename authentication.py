import hashlib

# Demo users
# These are only for the prototype.
USERS = {
    "admin": {
        "password": "admin123",
        "role": "Administrator"
    },
    "investigator": {
        "password": "investigator123",
        "role": "Investigator"
    },
    "viewer": {
        "password": "viewer123",
        "role": "Viewer"
    }
}

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()

def authenticate(username, password):
    if username not in USERS:
        return None
        
    if USERS[username]["password"] == password:
        return USERS[username]["role"]

    return None