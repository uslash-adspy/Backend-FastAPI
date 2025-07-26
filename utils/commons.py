import json
from fastapi import HTTPException

def find(text: str, target: str):
    for i in range(len(text)):
        if text[i:].startswith(target):
            return i
    return -1

def extract_dict(text: str):
   if find(text, "{") > 0:
       if find(text[::-1], "}") > 0:
           return json.loads(text[find(text, "{"):find(text[::-1], "}")])
   raise HTTPException(status_code=400, detail="Invalid dictionary format")
