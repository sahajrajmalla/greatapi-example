from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str

class BlogCreate(BlogBase):
    pass

class BlogSchema(BlogBase):
    id: int

    class Config:
        orm_mode = True
