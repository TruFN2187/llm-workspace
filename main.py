import json
import requests

def get_response(prompt: str, model: str = 'qwen3:8b', ctx: int = 10000) -> str:
    response = requests.post(
    'http://coruscant.local:11434/api/generate',
        json = {
            'model': model,
            'prompt': prompt,
            'stream': False,
            'options': {
                'num_ctx': ctx
            }
        }
    )

    data = response.json()

    if 'response' not in data:
        print('Unexpected output:', data)
        return ""
    
    return data['response']