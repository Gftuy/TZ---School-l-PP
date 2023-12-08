from typing import List

from fastapi import APIRouter
from .models import OutputGroup, ImputGroup, NewId
from .resolvers import add_new_group, get_group, get_groups, update_group, delete_current_group

router = APIRouter()


@router.get('/')
def get_auditorium() -> List[OutputGroup]:
    return get_groups()


@router.get('/{Auditorium_id}')
def get_current_auditorium(auditorium_id: int) -> OutputGroup:
    return get_group(group_id)


@router.post('/')
def add_group(new_group: ImputGroup) -> NewId:
    return add_new_group(new_group)


@router.put('/{Auditorium_id}')
def add_group(group_id: int, new_group: ImputGroup) -> NewId:
    return update_group(group_id, new_group)


@router.delete("/{Auditorium_id}")
def delete_group(group_id: int) -> NewId:
    return delete_current_group(group_id)