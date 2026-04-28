from datetime import datetime , timedelta, timezone
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt , JWTError
from app.core.config import settings

bearer_scheme = HTTPBearer()

def create_access_token(data : dict) -> str:

    """ Crea token firmado con fecha de expiracion"""

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.acces_token_expire_minutes)

    payload.update({"exp":expire})

    encoded_jwt = jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm
    )

    return encoded_jwt

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> str: 
    token = credentials.credentials

    
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],

        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
            )
        
        return username
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )
