import streamlit as st
from encoder import convert
import os

#st.button("Click me")
file = st.file_uploader('Upload an MP4', type='mp4', help='Upload an MP4')
if file:
    with st.spinner('Processing'):
        convert(file, f"480p_{file}")
    output_file = open('temp_videos/test_480p.mp4', "rb")

    st.download_button(
        label='Download MP4',
        data=output_file,
        mime='video/mp4',
        file_name="test_480.mp4",
        icon=":material/download:",
    )