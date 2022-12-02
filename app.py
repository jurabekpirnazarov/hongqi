import streamlit as st
from fastai.vision.all import *
import platform
import pathlib


plt = platform.system
if plt == "Linux": pathlib.WindowsPath = pathlib.PosixPath

st.title('jetour modellarini aniqlash')

file = st.file_uploader("rasm yuklash", type=['png','jpeg','jpg','gif','svg']) 

if file:
  st.image(file)
  model = load_learn('carsbestunehongqi.pkl')
  img = PILImage.create(file)
  pred , id, prob = model.predict(img)
  st.success(f'bashorat: {pred}')
