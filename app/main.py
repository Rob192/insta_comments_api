from fastapi import FastAPI
from app.src.find_comment import CommentFinder

commentFinder = CommentFinder()

app = FastAPI()

@app.get("/")
async def give_sentence(sentence: str):
    comment = commentFinder.find_comment(sentence)
    return comment