from sqlalchemy.orm import Session
from myapp.models import Blog
from myapp.schemas import BlogCreate

def create_blog(db: Session, blog: BlogCreate):
    new_blog = Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def read_blog(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()

def update_blog(db: Session, blog_id: int, blog: BlogCreate):
    existing_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if existing_blog:
        for key, value in blog.dict().items():
            setattr(existing_blog, key, value)
        db.commit()
        db.refresh(existing_blog)
    return existing_blog

def delete_blog(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog:
        db.delete(blog)
        db.commit()
    return blog

def list_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Blog).offset(skip).limit(limit).all()
