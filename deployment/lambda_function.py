#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('xception', target_size=(299, 299))

interpreter = tflite.Interpreter(model_path='bcd_xception.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = [
    'ct_healthy',
    'ct_tumor',
    'mri_glioma',
    'mri_healthy',
    'mri_meningioma',
    'mri_pituitary',
    'mri_tumor'
]

# url = 'https://raw.githubusercontent.com/Maxkaizo/mlzoomcamp_cp1/8a298f32f35f449b274b5cd76f47d375ca4abcc9/deployment/test_img_glioma.jpg'

def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result