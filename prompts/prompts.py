from typing import List
from fastapi import HTTPException

class PromptHandler():
    def __init__(self):
        prompts = []
        files = ["analyze", "question"]
        for filename in files:
            with open(f"./prompts/{filename}.md", "r", encoding='utf-8') as f:
                prompt = f.read()
            prompts.append(prompt)
        self.analyze_prompt = prompts[0]
        self.question_prompt = prompts[1]

    def get_analyze_prompt(self, post_content: List[str]):
        return self.analyze_prompt.format(
            post="\n".join(post_content)
        )

    def get_question_prompt(self):
        return self.question_prompt
