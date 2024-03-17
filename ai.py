import requests
def call_chatgpt_ai(user_query):
    api_key = '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'
    endpoint = 'https://api.openapi.comm/vl/engines/davinci/completions'
    headers = {
        'Content-Type':'application/json',
        'Authorization':f'Bearer {api_key}'
    }
    payload = {
        'prompt':user_query,
        'max_tokens': 50,
        'temperature': 0.7
    }
    response = requests.json()['choices'][0]['text']

user_query = "Can you recommend exercises for lower back pain?"
chatgpt_response = call_chatgpt_ai(user_query)
print(chatgpt_response)