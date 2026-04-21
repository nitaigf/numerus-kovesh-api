from fastapi import APIRouter, HTTPException, status

from app.schemas.numerology import NumerologyRequest, NumerologyResponse
from app.services.numerology_service import NumerologyService, NumerologyServiceError

router = APIRouter(prefix="/v1", tags=["numerology"])
service = NumerologyService()


@router.post("/numerology", response_model=NumerologyResponse)
def create_numerology(payload: NumerologyRequest) -> NumerologyResponse:
    try:
        return service.build_reading(payload.text)
    except NumerologyServiceError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"code": exc.code, "message": exc.message},
        ) from exc