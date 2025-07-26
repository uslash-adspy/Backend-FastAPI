from typing import Any, List, Dict

class AnalyzeResult():
    def __init__(self, category: str, isAd: bool, backAdPercentage: float, AdUrls: List[str]):
        self.category = category
        self.is_ad = isAd
        self.back_ad_percentage = backAdPercentage
        self.ad_urls = AdUrls

    def to_dict(self):
        return {
            "category": self.category,
            "is_ad": self.is_ad,
            "back_ad_percentage": self.back_ad_percentage,
            "ad_urls": self.ad_urls
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        analyze_result = cls(**data)
        return analyze_result
