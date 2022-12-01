#!/usr/bin/env python
# coding: utf-8

# will automatically be installed with pillow and tensorflow
import numpy as np
# will be installed via wheel from Alexey's github repo
import tflite_runtime.interpreter as tflite
# from keras_image_helper import create_preprocessor
# io and urrlib are part of python, so no need to pip install in docker file
from urllib import request
from io import BytesIO
# need to do pip install pillow in dockerfile
from PIL import Image


# preprocessor = create_preprocessor('xception', target_size=(299, 299))

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def preprocessor(url, target_size):

    img = download_image(url)
    img = prepare_image(img, target_size)
    # rescale image and convert to numpy array
    x = np.array(img)/255.
    # create a batch with a single image since this is the expected input to the model:
    X = np.array([x], dtype='float32')

    return X




interpreter = tflite.Interpreter(model_path='dino-vs-dragon-v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


# classes = [
#     'dress',
#     'hat',
#     'longsleeve',
#     'outwear',
#     'pants',
#     'shirt',
#     'shoes',
#     'shorts',
#     'skirt',
#     't-shirt'
# ]

# url = 'http://bit.ly/mlbookcamp-pants'

def predict(url):

    target_size = (150, 150)
    X = preprocessor(url, target_size)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    # return dict(zip(classes, float_predictions))
    return float_predictions


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result


