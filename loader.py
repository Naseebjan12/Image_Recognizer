import streamlit as st
from PIL.Image import Image
from image import image_recognizer
file_path=st.file_uploader(label='uplaod Your Image: ')
if file_path:
    st.image(file_path)
    st.header('Processing Your Image...')
    result=''    
    result=image_recognizer(file_path)
    if result:
        st.write(result)
