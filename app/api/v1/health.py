from fastapi import APIRouter

from app.api.v1.schema import HealthOut

router = APIRouter()


@router.get("/health", response_model=HealthOut)
def health() -> HealthOut:
    return HealthOut(status="ok")
