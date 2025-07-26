from fastapi import APIRouter, HTTPException
from schemas.analyze import AnalyzeRequest, AnalyzeResponse
from services.analyze import AnalyzeService

router = APIRouter(
    prefix="/analyze",
    tags=["Analyze"],
    responses={404: {"description": "Not found"}},
)

analyze_service = AnalyzeService()

@router.post("/", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    try:
        return AnalyzeResponse(
            **analyze_service.analyze_post(request.post).to_dict()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
