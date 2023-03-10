from pydantic import BaseModel


class ycitySchema(BaseModel):
    name: str
    about: str
    age: int
    img: str