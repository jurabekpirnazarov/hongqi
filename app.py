import streamlit as st
import fastai
import platform
import pathlib
import pickle
# load : get the data from file.
data = pickle.load(open('carsbestunehongqi.pkl', "rb"))
# loads : get the data from var


plt = platform.system()
if plt == "Linux": pathlib.WindowsPath = pathlib.PosixPath

st.title('jetour modellarini aniqlash')

file = st.file_uploader("rasm yuklash", type=['png','jpeg','jpg','gif','svg']) 

if file:
  st.image(file)
  img = PILImage.create(file)
  pred , id, prob = data.predict(img)
  st.success(f'bashorat: {pred}')
