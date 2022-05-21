from django.test import tag
from fastapi import APIRouter


from restapi.api.v1.endpoints import authentication, debug

api_router = APIRouter()

api_router.include_router(authentication.router, prefix='/auth', tags=['Authentication'])
api_router.include_router(debug.router, prefix='/debug', tags=['Debug'])