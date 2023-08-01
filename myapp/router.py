from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from greatapi.db.database import get_db
from myapp.schemas import BlogSchema, BlogCreate
from myapp.repository import (
    create_blog,
    read_blog,
    update_blog,
    delete_blog,
    list_blogs
)

from typing import List

meroapp_router = APIRouter(tags=["MyApp"])

@meroapp_router.post("/blogs/", response_model=BlogSchema)
def create_blog_route(blog: BlogCreate, db: Session = Depends(get_db)):
    return create_blog(db, blog)

@meroapp_router.get("/blogs/{blog_id}", response_model=BlogSchema)
def read_blog_route(blog_id: int, db: Session = Depends(get_db)):
    return read_blog(db, blog_id)

@meroapp_router.put("/blogs/{blog_id}", response_model=BlogSchema)
def update_blog_route(blog_id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    return update_blog(db, blog_id, blog)

@meroapp_router.delete("/blogs/{blog_id}", response_model=BlogSchema)
def delete_blog_route(blog_id: int, db: Session = Depends(get_db)):
    return delete_blog(db, blog_id)

@meroapp_router.get("/blogs/", response_model=List[BlogSchema])
def list_blogs_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return list_blogs(db, skip, limit)
