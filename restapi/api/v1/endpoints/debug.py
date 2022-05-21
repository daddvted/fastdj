from fastapi import Depends, APIRouter

from restapi.core.security import get_valid_user


router = APIRouter()


@router.get('/testlogin')
async def test_login(current_user: str = Depends(get_valid_user)):
    return {'msg': current_user}