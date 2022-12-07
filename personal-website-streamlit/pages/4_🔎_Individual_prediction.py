import streamlit as st
import matplotlib.pyplot as plt
import os
from utils.add_logo import add_logo

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Foodix-Individual-Prediction", page_icon=":corn:", layout="wide")
add_logo()
markdown = """
GitHub Repository: <https://github.com/MRL1998/MCK_Silos.git>
"""
st.sidebar.success("👆👆👆 Select a page above:")
st.sidebar.title("💻 Our work: ")
st.sidebar.info(markdown)

st.sidebar.title("📬 Contact:")
markdown = """
zidi.yang@hec.edu 
milos.basic@hec.edu
antoine.mellerio@hec.edu
camille.epitalon@hec.edu
augustin.de-la-brosse@hec.edu
michael.liersch@hec.edu
"""
st.sidebar.info(markdown)

# Main Body __________________________________________________________________________
with st.container():
    st.title("Individual Predictions 🔎")
    st.subheader("Upload your own pictures and apply the model to them")
    st.write(
        '''
           To upload an individual picture simply drag and drop it in the box.
        '''
    )

file_png = st.file_uploader("Upload a PNG image", type=([".png"]))

if file_png:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image(file_png)
        st.write("Uploaded picture")

    with col3:
        st.write(' ')

        
st.write(
        '''
        
           To upload an array of pictures please put in the path.
        '''
    )
path_folder = st.text_input('Path to image folder:')
st.write('You selected:', path_folder)   

