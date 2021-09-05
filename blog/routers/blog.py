from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import schemas,database,oaut2
import blog.repository.blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('',response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.repository.blog.get_all(db)

@router.post('',status_code =status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db:Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.repository.blog.create_blog(request,db)

@router.put('/{id}',status_code =status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog, db:Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.repository.blog.update(id,request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)    
def destroy(id:int,db: Session= Depends(database.get_db),get_current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.repository.blog.destroy(id,db)


@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def one(id:int,db:Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.repository.blog.one(id,db)      