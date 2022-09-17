from fastapi import Depends, APIRouter

from restapi.core.security import get_valid_user
from restapi.core.util import init_logger

LOG = init_logger(__name__)

router = APIRouter()


@router.get('/testlogin')
async def test_login(current_user: str = Depends(get_valid_user)):
    LOG.info("shiiiiit")
    
    return {'msg': current_user}