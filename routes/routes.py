from fastapi import APIRouter

vote_router = APIRouter(prefix="/vote")


@vote_router.post
def create_poll():
    pass
