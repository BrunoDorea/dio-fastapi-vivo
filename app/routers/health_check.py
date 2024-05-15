from fastapi import APIRouter

router = APIRouter(
    prefix="/health-check"
)

@router.get("/")
def health_check():
    return "OK"
