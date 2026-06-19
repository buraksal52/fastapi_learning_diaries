from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

"""
if request is = user/me, then output will be "user_id": me beacuse order is matter

"""