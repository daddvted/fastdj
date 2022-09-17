from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from jose import jwt, JWTError

from restapi.core import conf
from restapi.core.util import init_logger

LOG = init_logger(__name__)


oauth2 = OAuth2PasswordBearer(tokenUrl=f'{conf.API_PREFIX}/auth/token')

credentials_exception = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Invalid credential",
    headers={"WWW-Authenticate": "Bearer"},
)


def create_access_token(*, data: dict, expiration_delta: timedelta):
    data2decode = data.copy()

    if expiration_delta:
        expiration = datetime.utcnow() + expiration_delta
    else:
        expiration = datetime.utcnow() + timedelta(minutes=conf.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    data2decode.update({'exp': expiration})
    encoded_jwt = jwt.encode(data2decode, conf.SECRET_KEY, algorithm=conf.ALGORITHM)
    return encoded_jwt


def get_valid_user(token: str = Depends(oauth2)) -> str:
    try:
        payload = jwt.decode(token, conf.SECRET_KEY, algorithms=[conf.ALGORITHM])
        LOG.debug(payload)
        user = payload.get('user', None)

        if user is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    
    return user

