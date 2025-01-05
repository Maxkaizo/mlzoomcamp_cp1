# Brain Cancer Detection with Deep Learning

# Introduction

This repository contains the implementation of a machine learning model designed to detect brain cancer using CT and MRI images. This project is part of the final capstone for the Machine Learning Zoomcamp course offered by DataTalksClub.

# Objective (Value Proposition)
Brain cancer diagnosis is a critical medical task that typically requires expert analysis of imaging data. This project leverages machine learning techniques to assist in the detection of brain cancer from CT and MRI scans. The primary goal is to develop an accurate and efficient model that can identify cancerous images, offering a proof-of-concept for practical medical applications.

# Problem Definition (From a ML Perspective)
This project is framed as a Multiclass Classification Problem. The aim is to determine whether a patient's CT scan or MRI indicates the presence of a tumor. Furthermore, for MRI scans, the model aspires to identify the type of tumor when applicable.

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

For this project, I will use the Brain Tumor Multimodal Image (CT & MRI) dataset from Kaggle. This dataset includes a collection of scans sourced from multiple patients. According to its description:

    "The dataset includes high-resolution CT and MRI images captured from multiple patients, with each image labeled with the corresponding tumor type (e.g., glioma, meningioma, etc.) and its location within the brain. This combination of CT and MRI images aims to leverage the strengths of both imaging techniques: CT scans for clear bone structure visualization and MRI for soft tissue details, enabling a more accurate analysis of brain tumors."

This rich combination of imaging modalities offers a unique opportunity to develop a robust machine learning model that can effectively utilize the complementary strengths of CT and MRI scans.

# Transfer Learning References

https://keras.io/api/applications/
https://keras.io/guides/transfer_learning/




