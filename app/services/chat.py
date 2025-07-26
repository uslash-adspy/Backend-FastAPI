from typing import List
from anthropic import Anthropic
from fastapi import HTTPException
from prompts import PromptHandler
from utils import Secrets, Logger

logger = Logger()
secrets = Secrets()

class Pipeline():
    def __init__(self):
        self.client = Anthropic(api_key=secrets.anthropic_key)
        self.prompt_handler = PromptHandler()

    def question_post(self, chat: List[str], content: str):
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

class ChatService():
    def __init__(self):
        self.pipeline = Pipeline()

    def chat(self, chat: List[str], content: str):
        try:
            response = self.pipeline.question_post(chat, content)
            return response
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
