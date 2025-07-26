from typing import List
from anthropic import Anthropic
from fastapi import HTTPException
from app.models import AnalyzeResult
from prompts import PromptHandler
from utils import Secrets, Logger, extract_dict

logger = Logger()
secrets = Secrets()

class Pipeline():
    def __init__(self):
        self.client = Anthropic(api_key=secrets.anthropic_key)
        self.prompt_handler = PromptHandler()

    def analyze_post(self, post_content: List):
        analyze_prompt = self.prompt_handler.get_analyze_prompt(post_content)
        print(analyze_prompt)
        print("f")
        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=3000,
            messages=analyze_prompt
        )
        response_content = response.content[0].text
        print(response_content)
        print("u")
        analyze_result = extract_dict(response_content)
        print(analyze_prompt)
        return analyze_result

class AnalyzeService():
    def __init__(self):
        self.pipeline = Pipeline()

    def analyze_post(self, post_content: List) -> AnalyzeResult:
        try:
            print("t00")
            logger.info("k111")
            response = self.pipeline.analyze_post(post_content)
            analyze_result = AnalyzeResult.from_dict(response)
            return analyze_result
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
