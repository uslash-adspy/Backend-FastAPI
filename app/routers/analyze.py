from fastapi import APIRouter, HTTPException
from schemas.analyze import AnalyzeRequest, AnalyzeResponse, GetDataResponse
from services.analyze import AnalyzeService

router = APIRouter(
    prefix="/analyze",
    tags=["Analyze"],
    responses={404: {"description": "Not found"}},
)

analyze_service = AnalyzeService()

@router.get("/", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    try:
        ...
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
