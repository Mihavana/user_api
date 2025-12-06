from fastapi import FastAPI

app = FastAPI()

users = [{"id": 1, "nom": "Andry", "age": 23},
         {"id": 2, "nom": "Koto", "age": 40},
         {"id": 3, "nom": "Sarah", "age": 20},
]

@app.get('/')
def get_all_users():
    return {"data": users, "msg": "displayed successfully", "code": 200}

@app.get('/users/{user_id}')
def get_user_by_id(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return {"data": user, "msg": "user found", "code": 200}
    return {"data": None, "msg": "user not found", "code": 404}