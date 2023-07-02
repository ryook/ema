from pydantic import BaseModel


class RequestBody(BaseModel):
    text: str
