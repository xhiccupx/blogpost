from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from blog import schemas,models

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request:schemas.Blog,db: Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog     

def update(id:int,request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id as {id} not found ")
    blog.update(request.dict())
    db.commit()
    return {'details':f'the blog with id {id} is updated successfully'}    

def destroy(id:int,db: Session):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()

    return {'details':f'the blog with id {id} is deleted successfully'} 

def one(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id as {id} not found ")
    return blog             