from pydantic import BaseModel

from typing import List


class Response(BaseModel):
    vec: List[float]
