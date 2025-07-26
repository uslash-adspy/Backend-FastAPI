from typing import List
from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    post: List[str]

class AnalyzeResponse(BaseModel):
    category: str # 카테고리
    isAd: bool # 광고 여부
    backAdPercentage: float # 한 자리수 소수 - 뒷광고 확률
    adProbability: float # 한 자리 소수 - 종합 평가 광고 확률
    AdUrls: List[str] # 제휴 광고 URLs
    comment: str # 이게 광고인 이유 또는 코멘트
