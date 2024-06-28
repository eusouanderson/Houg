from tinydb import TinyDB, Query
import hashlib

# Inicializa o banco de dados
db = TinyDB('db.json')
User = Query()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str, name: str, telephone: str):
    if db.search(User.username == username):
        return {"message": "Usuario ja existe"}

    db.insert({"username": username, "password": hash_password(password), "name": name, "telephone": telephone})
    return {"message": "Usuario criado"}

def login_user(username: str, password: str):
    hashed_password = hash_password(password)
    if db.search((User.username == username) & (User.password == hashed_password)):
        return {"message": "Login bem sucedido"}
    else:
        return {"message": "Usuario ou senha invalidos"}


