from fastapi import APIRouter, Depends, Query
from queries.dashboard import TodoIn, TodoOut, TodoRepository
from typing import List


router = APIRouter()


@router.get("/dashboard/", response_model=List[TodoOut])
def get_all_todos(
    user_id: int,
    repo: TodoRepository = Depends(),
) -> List[TodoOut]:
    return repo.get_all(user_id)

@router.delete("/dashboard/{todo_id}/")
def delete_todo(
    todo_id: int,
    repo: TodoRepository = Depends(),
) -> bool:
    return repo.delete(todo_id)
