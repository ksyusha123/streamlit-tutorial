import streamlit as st
import requests
from PIL import Image

API_URLS = {
    'efficient-b7': 'https://api-inference.huggingface.co/models/google/efficientnet-b7',
    'resnet-18': 'https://api-inference.huggingface.co/models/microsoft/resnet-18'
}

headers = {"Authorization": "Bearer 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"}

def query(data, model_name):
    response = requests.post(API_URLS[model_name], headers=headers, data=data)
    return response.json()

def input_features():
    return st.selectbox('Модель', API_URLS.keys())

def predict(model_name, data):
    result = query(data, model_name)
    return result

def inference(model_name, upload):
    c1, c2 = st.columns(2)
    if upload:
        output = predict(model_name, upload)
        image = Image.open(upload)
        c1.header('Input Image')
        c1.image(image)
        c2.header('Predicted class: ')
        c2.write(output[0]['label'])

def show_main_page():
    st.set_page_config(page_title='Two Models Inference')
    st.title('Распознавание объектов')
    model_name = input_features()
    st.header('Загрузите картинку')
    upload = st.file_uploader('Выберите картинку', type=['png', 'jpg'])
    inference(model_name, upload)

show_main_page()
