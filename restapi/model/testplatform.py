from typing import Optional
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    name: str = Field(..., title='Project name')
    description: Optional[str]
    owner: Optional[str]
    planned: bool = Field(default=False)
    phase: Optional[str]


class ProjectOut(ProjectBase):
    # id: int
    pk: int


class MilestoneBase(BaseModel):
    name: str = Field(..., title='Milestone name')
    description: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    project: int


class MilestoneOut(MilestoneBase):
    id: int


class CaseBase(BaseModel):
    name: str = Field(..., title='Case name')
    description: Optional[str]
    owner: Optional[str]
    automated: bool = Field(default=False)


class CaseOut(CaseBase):
    id: int


class PlanBase(BaseModel):
    case: int
    milestone: int
    plan_to_exec: Optional[datetime]
    plan_to_end: Optional[datetime]

class PlanOut(PlanBase):
    id :int


class ResultEnum(int, Enum):
    passed = 0
    failed = 1

class ResultBase(BaseModel):
    status: ResultEnum
    tester: Optional[str]
    case_name: Optional[str]
    project_name: Optional[str]
    completed_date: Optional[datetime]
    in_plan: Optional[bool]

    plan: int

class ResultOut(ResultBase):
    id: int
