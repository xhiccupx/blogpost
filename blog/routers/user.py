from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog import schemas,database
import blog.repository.user
from blog import oaut2

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('')
def create_user(request: schemas.User,db:Session = Depends(database.get_db)):
    return blog.repository.user.create_user(request,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowUser)
def get_user(id:int,db:Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.repository.user.get_user(id,db)    
