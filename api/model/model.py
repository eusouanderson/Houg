from pydantic import BaseModel

class UserInput(BaseModel):
    username: str
    password: str