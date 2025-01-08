import requests

url = 'https://wx2naanqv2.execute-api.us-east-1.amazonaws.com/test_stage/detect'

data = {'url': 'https://raw.githubusercontent.com/Maxkaizo/mlzoomcamp_cp1/8a298f32f35f449b274b5cd76f47d375ca4abcc9/deployment/test_img_glioma.jpg'}

# API Key
api_key = 'API_KEY_HERE'

headers = {
    'x-api-key': api_key
}

result = requests.post(url, json=data, headers=headers).json()

print(result)