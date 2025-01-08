import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'


data = {'url': 'https://raw.githubusercontent.com/Maxkaizo/mlzoomcamp_cp1/8a298f32f35f449b274b5cd76f47d375ca4abcc9/deployment/test_img_glioma.jpg'}

result = requests.post(url, json=data).json()
print(result)