from fastapi import FastAPI
#from app.src.find_comment import CommentFinder

app = FastAPI()

# commentFinder = CommentFinder()

@app.get("/")
async def give_sentence(sentence: str):
    comment = sentence #commentFinder.find_comment(sentence)
    return {"comment": comment}