import streamlit as st
from fastai.vision.all import *

st.title('jetour modellarini aniqlash')

file = st.file_uploader("rasm yuklash", type=['png','jpeg','gif','svg']) 

if file:
  st.image(file)
  model = load_learner('carsbestunehongqi.pkl')
  img = PILImage.create(file)
  pred , id, prob = model.predict(img)
  st.success(f'bashorat: {pred}')
  
  
