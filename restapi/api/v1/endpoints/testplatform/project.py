from typing import List
from fastapi import Depends, APIRouter

from restapi.core.security import get_valid_user
from restapi.core.util import convert_django_model
from restapi.model.testplatform import ProjectOut

from apps.testplatform.models import Project


router = APIRouter()


@router.get('/project', response_model=List[ProjectOut])
async def get_projects():
    all = Project.objects.all()
    # print(all)
    # tmp = convert_django_model(all)
    # print(tmp)
    # return ""
    return convert_django_model(all)