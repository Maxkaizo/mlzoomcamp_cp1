# Brain Cancer Detection with Deep Learning
![Banner](image.png)
# Introduction

This repository contains the implementation of a machine learning model designed to detect brain cancer using CT and MRI images. This project is part of the final capstone for the Machine Learning Zoomcamp course offered by DataTalksClub.

# Objective (Value Proposition)
Brain cancer diagnosis is a critical medical task that typically requires expert analysis of imaging data. This project leverages machine learning techniques to assist in the detection of brain cancer from CT and MRI scans. The primary goal is to develop an accurate and efficient model that can identify cancerous images, offering a proof-of-concept for practical medical applications.

# Problem Definition (From a ML Perspective)
This project is framed as a Multiclass Classification Problem. The objective is to determine whether a patient's CT scan or MRI indicates the presence of a tumor. Additionally, for MRI scans, the model aims to classify the type of tumor when applicable.

To achieve this, I will build a model based on a Convolutional Neural Network (CNN) and employ the transfer learning technique. Specifically, I will utilize the Xception model, which has been pre-trained on the ImageNet dataset. By leveraging Xception's feature extraction capabilities, I can fine-tune the model using the dataset's images to optimize it for this task.

So, the model will consists of three main components: 

1. A feature extraction layer using Xception pre-trained model to generate feature maps from the input images
2. A dense neural network layer to identify and refine patterns from these features
3. And a probabilistic classifier with a softmax activation to output the probabilities for each class in the multiclass classification task. 

In the serving phase, the input will be an image, and the output will represent the probabilities of the image belonging to each class.

# Repository Structure

    mlzoomcamp_cp1/
    |-- Dataset/             # Dataset (train, test and validation splits)
    |-- notebooks.ipynb      # Data preparation, EDA, Model Selection, and Parameter Tuning
    |-- references/          # Relevant contextual information
    |-- models/              # Saved models and weights
    |-- README.md            # Project overview
    |-- requirements.txt     # Dependencies         ***** placeholder ******

# Domain Context
If you need (as I did) some context regarding the referred medical procedures, what is a CT Scan and an MRI, I'm including some definitions [here](https://github.com/Maxkaizo/mlzoomcamp_cp1/blob/main/references/Domain_Context.md)

# Dataset
For this project, I will use the [Brain Tumor Multimodal Image (CT & MRI) dataset](https://www.kaggle.com/api/v1/datasets/download/murtozalikhon/brain-tumor-multimodal-image-ct-and-mri) from Kaggle. This dataset includes a collection of scans sourced from multiple patients. According to its description:

    "The dataset includes high-resolution CT and MRI images captured from multiple patients, with each image labeled with the corresponding tumor type (e.g., glioma, meningioma, etc.) and its location within the brain. This combination of CT and MRI images aims to leverage the strengths of both imaging techniques: CT scans for clear bone structure visualization and MRI for soft tissue details, enabling a more accurate analysis of brain tumors."

This rich combination of imaging modalities offers a unique opportunity to develop a robust machine learning model that can effectively utilize the complementary strengths of CT and MRI scans.

# Script train.py (suggested name)
- Training the final model
- Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)

# Script predict.py (suggested name)
- Loading the model
- Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)

# Files with dependencies
- Pipenv and Pipenv.lock if you use Pipenv
- or equivalents: conda environment file, requirements.txt or pyproject.toml

# Dockerfile for running the service

# Deployment
- URL to the service you deployed or
- Video or image of how you interact with the deployed service

# Potential Improvements:

Probar entrenando de cero el modelo
probar usando un modelo de dominio especifico en el ambito médico
- Test the model further with a holdout dataset or through cross-validation to ensure robust performance.