import logging
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED


from django.contrib.auth import authenticate

from restapi.model.auth import Token
from restapi.core.security import create_access_token
from restapi.core.util import init_logger
from restapi.core import conf 

LOG = init_logger(__name__)

router = APIRouter()


@router.post('/token', response_model=Token, name="Token")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    user = authenticate(username=username, password=password)


    if user:
        access_token_expires = timedelta(minutes=conf.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={
            "user": username,
            # "domain": domain,
            }, expiration_delta=access_token_expires
        )

        # role = await get_role(username, domain)
        # return {"access_token": access_token, "token_type": "bearer", "role": role, "domain": domain}
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        LOG.error("Incorrect username or password")
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )



