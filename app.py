import streamlit as st
import fastai

st.title('jetour modellarini aniqlash')

st.file_uploader("rasm yuklash", type=['png','jpeg','gif','svg']) 

model = load_learner('carsbestunehongqi.pkl')

