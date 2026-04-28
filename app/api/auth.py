from fastapi import APIRouter, HTTPException, Depends

from app.core.config import settings
from app.core.security import create_access_token, get_current_user
from app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(payload : LoginRequest):

    if (payload.username != settings.auth_username or payload.password != settings.auth_password):

        raise HTTPException(status_code=401,detail="Invalid Credentials")
    
    token = create_access_token(data={"sub" : payload.username})

    return {
        "access_token" : token,
        "token_type" : "bearer",
    }

@router.get("/me")
def get_me(current_user : str = Depends(get_current_user)):
    return {"username" : current_user}