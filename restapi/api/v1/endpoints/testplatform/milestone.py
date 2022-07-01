from typing import List
from fastapi import Depends, APIRouter

from restapi.core.security import get_valid_user
from restapi.core.util import convert_django_model
from restapi.model.testplatform import MilestoneOut

from apps.testplatform.models import  Milestone


router = APIRouter()


@router.get('/milestone', response_model=List[MilestoneOut])
async def get_milestones():
    all = Milestone.objects.all()
    print(all)
    return convert_django_model(all)