from fastapi import APIRouter, HTTPException
from schemas.analyze import AnalyzeRequest, AnalyzeResponse
from services.analyze import AnalyzeService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
    responses={404: {"description": "Not found"}},
)

analyze_service = AnalyzeService()

@router.get("/{url}/", response_model=AnalyzeResponse)
async def analyze(url: str):
    try:
        ...
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
