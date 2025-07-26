import re, json, ast
from fastapi import HTTPException

def find(text: str, target: str):
    for i in range(len(text)):
        if text[i:].startswith(target):
            return i
    return -1

def extract_dict(text: str):
    cleaned = text.strip()
    
    cleaned = re.sub(r'^```(?:json)?\s*\n?', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\n?```\s*$', '', cleaned)
    
    start_brace = cleaned.find('{')
    start_bracket = cleaned.find('[')
    if start_brace == -1 and start_bracket == -1:
        raise ValueError("JSON 구조를 찾을 수 없음")
    
    start = min(x for x in [start_brace, start_bracket] if x != -1)
    cleaned = cleaned[start:]
    
    end_brace = cleaned.rfind('}')
    end_bracket = cleaned.rfind(']')
    end = max(end_brace, end_bracket)
    if end != -1:
        cleaned = cleaned[:end + 1]
    
    cleaned = re.sub(r'["""]', '"', cleaned)
    cleaned = re.sub(r"'([^']*)':", r'"\1":', cleaned)
    cleaned = re.sub(r":\s*'([^']*)'", r': "\1"', cleaned)
    cleaned = re.sub(r':\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*([,}])', r': "\1"\2', cleaned)
    cleaned = re.sub(r',(\s*[}\]])', r'\1', cleaned)
    cleaned = re.sub(r':\s*(NaN|undefined|Infinity)\s*([,}])', r': null\2', cleaned)
    cleaned = re.sub(r'\\n\s+', ' ', cleaned)
    cleaned = re.sub(r'\\"', '"', cleaned)
    cleaned = re.sub(r":\s*\"([^\"]*\\n[^\"]*)\"\s*", lambda m: ': "' + m.group(1).replace('\\n', ' ').replace('\\"', '"') + '"', cleaned)
    
    try:
        return json.loads(cleaned)
    except:
        try:
            return ast.literal_eval(cleaned)
        except:
            raise ValueError(f"JSON 파싱 실패: {cleaned[:100]}...")