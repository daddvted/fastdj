from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED


from django.contrib.auth import authenticate

from restapi.model.auth import Token
from restapi.core import conf 


router = APIRouter()



@router.post('/events')
async def gerrit_web_hook(request):
    print(request.body())