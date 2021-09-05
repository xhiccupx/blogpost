from fastapi import APIRouter, Depends, status ,HTTPException
from blog import schemas, database, models, mytoken 
from blog.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid credentials")
    if not Hash.verify(request.password,user.password):   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
    access_token = mytoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}