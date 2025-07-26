from typing import Any, List, Dict

class AnalyzeResult():
    def __init__(self, category: str, isAd: bool, backAdPercentage: float, adProbability: float, adUrls: List[str], comment: str):
        self.category = category
        self.is_ad = isAd
        self.back_ad_percentage = backAdPercentage
        self.ad_probability = adProbability
        self.ad_urls = adUrls
        self.comment = comment

    def to_dict(self):
        return {
            "category": self.category,
            "isAd": self.is_ad,
            "backAdPercentage": self.back_ad_percentage,
            "adProbability": self.ad_probability,
            "adUrls": self.ad_urls,
            "comment": self.comment
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        analyze_result = cls(**data)
        return analyze_result
