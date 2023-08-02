from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int  # Add the user_id field to represent the foreign key relationship


class BlogCreate(BlogBase):
    pass

class BlogSchema(BlogBase):
    id: int


    class Config:
        orm_mode = True
