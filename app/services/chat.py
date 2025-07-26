from typing import List, Dict
from anthropic import Anthropic
from fastapi import HTTPException
from schemas import Message
from prompts import PromptHandler
from utils import Secrets, Logger, extract_dict

logger = Logger()
secrets = Secrets()

class Pipeline():
    def __init__(self):
        self.client = Anthropic(api_key=secrets.anthropic_key)
        self.prompt_handler = PromptHandler()

    def question_post(self, chat: List[Message], content: str):
        parsed_chat = []
        for message in chat:
            parsed_chat.append({"role": message.role, "content": message.content})
        question_prompt = self.prompt_handler.get_question_prompt()
        internal_chat = parsed_chat.copy()
        parsed_chat.append({"role": "user", "content": content})
        # internal_chat.append({"role": "system", "content": question_prompt})
        internal_chat.append({"role": "user", "content": content})
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=internal_chat,
            system=question_prompt
        )
        response_content = response.content[0].text
        response = extract_dict(response_content)
        return response

class ChatService():
    def __init__(self):
        self.pipeline = Pipeline()

    def chat(self, chat: List[Message], content: str):
        try:
            response = self.pipeline.question_post(chat, content)
            return response
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
