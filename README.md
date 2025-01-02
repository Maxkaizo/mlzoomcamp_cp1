# Brain Cancer Detection with Deep Learning

# Introduction

In this project, I'll implement a brain cancer detection system using CT and MRI images, leveraging the potential of various Machine Learning and Deep Learning algorithms and tools. I'll document all data processing in the [notebook.ipynb]() file and all additional or context information will be here in the README.MD

# Problem Description
Brain cancer is one of the most critical and life-threatening medical conditions, requiring precise and timely diagnosis to improve treatment outcomes and patient survival rates. Traditional diagnostic approaches often rely on manual interpretation of CT and MRI scans by radiologists, which can be time-consuming, subjective, and prone to errors due to the complexity and variability of tumor presentations.

This project aims to address the challenge of automating brain tumor detection and classification by developing a deep learning-based solution. The objective is to create a system capable of accurately identifying brain tumors from multimodal imaging data (CT and MRI scans) and classifying them into specific tumor types. By integrating cutting-edge Machine Learning and Deep Learning techniques, the project seeks to enhance diagnostic accuracy and efficiency, ultimately aiding healthcare professionals in decision-making processes.

# Domain Context

In order to have a base understanding of the aforementioned methods, here are some definitions and references

## CT Scan

A CT Scan, or Computed Tomography Scan, is a medical imaging technique that uses X-rays combined with computer processing to create detailed cross-sectional images of the body. It provides a quick and effective way to visualize internal structures such as bones, organs, and tissues. CT Scans are commonly used for detecting abnormalities like tumors or masses but lack the level of tissue differentiation needed to classify specific types of conditions, making them ideal for initial diagnoses or general assessments.

- Uses X-rays to create cross-sectional images of the body.
- Primarily detects general abnormalities, such as masses or tumors, without providing detailed tissue differentiation.

[What is a CT scan? | Ohio State Medical Center](https://www.youtube.com/watch?v=NzZyd2eSRss)

## Magnetic Resonance Imaging (MRI) 

Magnetic Resonance Imaging (MRI) is a medical imaging technique that uses strong magnetic fields and radio waves to produce highly detailed images of the body's internal structures, particularly soft tissues. Unlike CT Scans, MRI does not use ionizing radiation, making it safer for repeated use. It is especially effective for visualizing the brain, spinal cord, and other complex tissues, enabling the precise identification and classification of conditions such as tumors, making it a critical tool in diagnosing and monitoring neurological and musculoskeletal disorders.

- Uses magnetic fields and radio waves to produce detailed images, especially of soft tissues.
- Provides higher precision for identifying specific types of tumors compared to CT Scans.

[What is an MRI? | Ohio State Medical Center](https://www.youtube.com/watch?v=K9T1v4lWWF4)

---

### **Tumor Types Identified in MRI:**
- **Glioma:**
  - Tumors originating from glial cells in the brain or spinal cord.
  - Can range from low-grade to highly malignant (e.g., glioblastoma).

- **Meningioma:**
  - Tumors that develop in the meninges, the protective layers covering the brain and spinal cord.
  - Typically benign but can exert pressure on surrounding structures.

- **Pituitary Tumor:**
  - Tumors located in the pituitary gland at the brain's base.
  - Often benign but may disrupt hormonal functions.

- **Tumor (Generic):**
  - A broader category for cases where the tumor type is unspecified or does not fall into the above classifications. 

This structure provides the foundation for understanding the dataset and preparing it for further preprocessing and modeling.

# Dataset 
I'll use the [Brain tumor multimodal image (CT & MRI)](https://www.kaggle.com/datasets/murtozalikhon/brain-tumor-multimodal-image-ct-and-mri/code) dataset from kaggle wich includes a collection of scans included in several sources, as stated in its description "the dataset includes high-resolution CT and MRI images captured from multiple patients, with each image labeled with the corresponding tumor type (e.g., glioma, meningioma, etc.) and its location within the brain. This combination of CT and MRI images aims to leverage the strengths of both imaging techniques: CT scans for clear bone structure visualization and MRI for soft tissue details, enabling a more accurate analysis of brain tumors".




