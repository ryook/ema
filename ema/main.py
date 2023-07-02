from fastapi import FastAPI

from .schemas.request import RequestBody
from .schemas.response import Response
from .usecases.japanese_embedding_service import JapaneseEmbeddingService

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/embedding")
async def embedding(param: RequestBody):
    text = param.text
    vec = JapaneseEmbeddingService.embedding(text)
    return Response(vec=vec)
