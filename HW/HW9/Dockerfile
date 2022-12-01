# base python image of 3.9 to match the python and tensorflow version with which the dino-vs-dragon model was compiled
# FROM public.ecr.aws/lambda/python:3.9
FROM svizor42/zoomcamp-dino-dragon-lambda:v2

# using code from pillow
# RUN pip install keras-image-helper
RUN pip install pillow
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl?raw=true

# since already present, no need
# COPY dino-vs-dragon-v2.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]