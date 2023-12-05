USERS = [
    ("admin", "123123"),
    ("user", "123123"),
    ("bia", "123123")
]

def login(username, password):
    for user in USERS:
        if(user[0] == username and user[1] == password):
            return True
    return False