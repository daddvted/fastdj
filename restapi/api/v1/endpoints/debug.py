from fastapi import Depends, APIRouter

from restapi.core.security import get_valid_user
from restapi.core.util import init_logger

LOG = init_logger(__name__)

router = APIRouter()


@router.get('/logintest')
async def login_test(current_user: str = Depends(get_valid_user)):
    LOG.info("shiiiiit")
    print("shiiiit")
    
    return {'msg': current_user}