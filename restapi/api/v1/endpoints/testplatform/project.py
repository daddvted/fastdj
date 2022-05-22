from fastapi import Depends, APIRouter

from restapi.core.security import get_valid_user
from restapi.core.util import convert_django_model

from apps.testplatform.models import Project

router = APIRouter()


@router.get('/project')
async def get_project():
    all = Project.objects.all()
    print(all)
    return convert_django_model(all)