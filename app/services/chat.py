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

    def question_post(self, chat: List, content: str):
        question_prompt = self.prompt_handler.get_question_prompt()
        internal_chat = chat.copy()
        chat.append({"role": "user", "content": content})
        internal_chat.append({"role": "system", "content": question_prompt})
        internal_chat.append({"role": "user", "content": content})
        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=1500,
            messages=internal_chat
        )
        response_content = response.content[0].text
        return response_content

class AnalyzeService():
    def __init__(self):
        self.pipeline = Pipeline()
        self.chats = {}

    def analyze_post(self, url: str, content: str):
        try:
            if url not in self.chats:
                ...
            response = self.pipeline.question_post(self.chats[url], content)
            return response
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
