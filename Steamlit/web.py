import streamlit as st
import pandas as pd
import numpy as np
import cv2 as cv


st.title('Dog vs Cat')
st.subheader('Classifing image using CNN')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    btn = st.button('Classify',)

if uploaded_file:
    st.image(uploaded_file, width=256,)


