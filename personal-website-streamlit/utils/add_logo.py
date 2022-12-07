import streamlit as st
from PIL import Image
import base64
import streamlit as st

"""
    add_logo(): 
        Usecase: CSS code that changes layout of the sidebar, puts a logo and a title in place.
        Input: ____
        Output: Returns markdown with Logo and Company Name above pages

"""

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/298/ear-of-corn_1f33d.png);
                background-repeat: no-repeat;
                padding-top: 60px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Foodix";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )