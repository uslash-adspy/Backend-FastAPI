import os
from dotenv import load_dotenv

env_path = ".env"
load_dotenv(dotenv_path=env_path)

class Secrets():
    def __init__(self):
        self.anthropic_key = os.getenv("Anthropic_KEY")
