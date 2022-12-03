import streamlit as st
import fastai
import platform
import pathlib

plt = platform.system()
if plt == "Linux": pathlib.WindowsPath = pathlib.PosixPath
 
st.title('Jetour modellarini aniqlash')

file = st.file_uploader("rasm yuklash", type=['png','jpeg','jpg','gif','svg']) 

if file:
  st.image(file)
  data = load_learner('https://github.com/jurabekpirnazarov/hongqi/blob/main/carsbestunehongqi.pkl')
  img = PILImage.create(file)
  pred , id, prob = data.predict(img)
  st.success(f'bashorat: {pred}')
