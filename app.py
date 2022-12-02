import streamlit as st
import fastai
import platform
import pathlib


plt = platform.system()
if plt == "Linux": pathlib.WindowsPath = pathlib.PosixPath

st.title('jetour modellarini aniqlash')

file = st.file_uploader("rasm yuklash", type=['png','jpeg','jpg','gif','svg']) 

if file:
  st.image(file)
  model = load_learner('carsbestunehongqi.pkl')
  img = PILImage.create(file)
  pred , id, prob = model.predict(img)
  st.success(f'bashorat: {pred}')
