from fastapi import FastAPI, HTTPException, Depends
from app.schema import PostCreate
from app.db import create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create database tables
    await create_db_and_tables()
    yield
    # Shutdown: cleanup if needed


app = FastAPI(lifespan=lifespan)


text_posts = {"1": {"title": "New posts", "content": "Content of the post"}}

@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post_by_id(id: str):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")  
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    # Generate next ID as string
    next_id = str(int(max(text_posts.keys())) + 1)
    text_posts[next_id] = new_post
    return {"id": next_id, **new_post}
