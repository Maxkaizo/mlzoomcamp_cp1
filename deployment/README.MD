# Deployment Documentation

## Introduction

The architecture consists of two main components:

- Local Environment: A Docker container that packages the model and necessary scripts, allowing local testing before cloud deployment.
- Cloud Environment: The service is deployed on AWS Lambda using Amazon Elastic Container Registry (ECR) as the container repository and API Gateway for external access.

Solution Architecture

Base Image: This solution uses a pre-configured base image provided by Amazon for Lambda functions. The base image simplifies the deployment by including necessary scripts and configurations to handle Lambda's runtime requirements.

Official documentation for Lambda base images: [AWS Lambda Python Base Image](https://gallery.ecr.aws/lambda/python)

Model: The machine learning model (bcd_xception.tflite) is optimized for TensorFlow Lite and packaged within the container.
API Gateway: Exposes the Lambda function as a RESTful endpoint, enabling external HTTP requests.

Security: API requests are authenticated using an API key.

## Deployment

This project supports both local and cloud deployment. Each includes instructions for setup and testing.

### 1. Local Deployment
Setup Instructions
Clone the repository:
bash
Copiar código
git clone https://github.com/Maxkaizo/mlzoomcamp_cp1.git
Navigate to the deployment folder:
bash
Copiar código
cd mlzoomcamp_cp1/deployment
Build the Docker image:
bash
Copiar código
docker build -t bcd_mlzoomcamp .
Run the Docker container:
bash
Copiar código
docker run -it --rm -p 8080:8080 bcd_mlzoomcamp
Local Testing
Once the container is running, send a POST request to http://localhost:8080/2015-03-31/functions/function/invocations to test the service. Use the following Python script:

python
Copiar código
import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://raw.githubusercontent.com/Maxkaizo/mlzoomcamp_cp1/8a298f32f35f449b274b5cd76f47d375ca4abcc9/deployment/test_img_glioma.jpg'}

result = requests.post(url, json=data).json()

print(result)
2. Cloud Deployment
Setup Instructions
Create an ECR Repository

Run the following command to create an Amazon ECR repository where the Docker image will be stored:

bash
Copiar código
aws ecr create-repository --repository-name bcd_cp_repo
Example output:

json
Copiar código
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:123456789012:repository/bcd_cp_repo",
        "registryId": "123456789012",
        "repositoryName": "bcd_cp_repo",
        "repositoryUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/bcd_cp_repo",
        "createdAt": "2025-01-08T11:29:27.048000-06:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
Log in to Amazon ECR

Authenticate Docker to interact with your ECR repository. Replace the region and account ID with your details:

bash
Copiar código
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
Example output:

Copiar código
Login Succeeded
Push the Docker Image to ECR

Tag the Docker image:
bash
Copiar código
docker tag bcd_mlzoomcamp:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/bcd_cp_repo:brain_cancer_model-exception-v1
Push the image to ECR:
bash
Copiar código
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/bcd_cp_repo:brain_cancer_model-exception-v1
Deploy the Docker Image to Lambda

Create a new Lambda function.
Select Container Image as the deployment type.
Use the image URI from ECR to configure the Lambda function.
Configure an API Gateway

Create an HTTP API Gateway.
Link it to the Lambda function.
Generate an API key to secure the endpoint.
Cloud Testing
Use the following Python script to test the deployed service on AWS:

python
Copiar código
import requests

# API Gateway endpoint
url = 'https://wx2naanqv2.execute-api.us-east-1.amazonaws.com/test_stage/detect'

# Input data (image URL)
data = {'url': 'https://raw.githubusercontent.com/Maxkaizo/mlzoomcamp_cp1/8a298f32f35f449b274b5cd76f47d375ca4abcc9/deployment/test_img_glioma.jpg'}

# API key
api_key = 'API_KEY_HERE'

# Request headers
headers = {
    'x-api-key': api_key
}

# Send POST request
result = requests.post(url, json=data, headers=headers).json()

print(result)


Note: Replace API_KEY_HERE with the actual API key. Contact me via Slack (@Maxkaizo) or email (pptmtz@gmail.com) to obtain the API key.


## Testing the service

### Locally

To test the the model locally , follow this instructions:

1. Clone this repository

```
git clone https://github.com/Maxkaizo/mlzoomcamp_cp1.git
```
2. Move to the deployment folder

```
cd mlzoomcamp_cp1/deployment
```
3. Build a docker image

```
docker build -t bcd_mlzoomcamp .
```
4. Run the docker image

```
docker run -it --rm -p 8080:8080 bcd_mlzoomcamp
```