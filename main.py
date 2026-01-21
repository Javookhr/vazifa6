from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI()

@app.get("/")
def hello() -> dict:
    return {"message": "hello world"}

user = [
    {"id": 1, "name": "Javohir", "adres": "Fergana"},
    {"id": 2, "name": "Aziza", "adres": "Andijon"},
    {"id": 3, "name": "Bobur", "adres": "Samarqand"},
    {"id": 4, "name": "Dilnoza", "adres": "Qashqadaryo"},
    {"id": 5, "name": "Eldor", "adres": "Namangan"},
]


@app.get("/user/")
def read_user() -> list:
    return user


@app.get("/user/{user_id}/")
def read_id(user_id: Annotated[int, Path(ge=1)]) -> dict:
    for u in user:
        if u.get("id") == user_id:
            return u
    return {"error": "User not found"}

@app.get("/user/adres/{adres}/")
def read_user(adres: str) -> list:
    found_users = []
    for u in user:
        if u.get("adres").lower() == adres.lower():
            found_users.append(u)
    
    if len(found_users) == 0:
        return {"error": "Users not found"}
    
    return found_users

@app.post("/user/")
def create_user(name: str, adres: str) -> dict:
    user.append(
        {
            "id": len(user) + 1,
            "name": name,
            "adres": adres
        }
    )
    return {"message": "User created successful!"}

if __name__ == "__main__":
    uvicorn.run(app, port=8001)