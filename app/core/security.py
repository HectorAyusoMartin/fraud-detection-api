from datetime import datetime , timedelta, timezone
from jose import jwt 
from app.core.config import settings

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