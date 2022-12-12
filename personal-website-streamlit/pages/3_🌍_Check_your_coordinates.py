import streamlit as st
import utils
import plotly.figure_factory as ff
import numpy as np
import io
from PIL import Image
import leafmap.foliumap as leafmap
import os 
import cv2
from utils.add_logo import add_logo2
import matplotlib.pyplot as plt
import tensorflow as tf
from utils.classif import classif_silo
from utils.segment import segment_silo
import pandas as pd


classif_model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'models/classification_model'))
segment_model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'models/segmentation_model'))

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Foodix-Coordinates", page_icon=":corn:", layout="wide")
add_logo2("images/geosilo_logo.png")
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
st.title("Check your Coordinates 🌍")
st.subheader("Select any coordinates in the world amd check for Silos")

st.write("""
         How it works
         - Insert the coordinates of the farm you wish to check, press Enter
         - The map will autolocate itself and crop the image (100m x 100m)
         - The image is processed and analyzed by the classification and segmentation model
         """
        )
st.write("---")
st.subheader("Interactive Map")

# Coordinates: Calculation and Transformation _________________________________________
coordinates_langitude, coordinates_longitude = 48.8566, 2.3522
coordinates= st.text_input('Put in your cordinates:')

# Demonstration coordinates: 48.26442272491014, 1.1918271949748058
if coordinates == "":
    coordinates = (44.677973243540535, -114.06776247576822)
else:
    coordinates = coordinates.replace(',', "")
    coordinates = coordinates.split(" ")
    coordinates = [float(x) for x in coordinates]
    coordinates = (coordinates[0], coordinates[1])
    
top_left_coordinates = utils.top_left_coordinates(coordinates[0], coordinates[1])
bottom_right_coordinates = utils.bottom_right_coordinates(coordinates[0], coordinates[1])

# Map ______________________________________________________________________________
api_key = os.environ.get("HEREMAPS_API_KEY")
m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True, google_map="HYBRID",
                api_key=api_key, center=coordinates, zoom=18)

# m.add_basemap(basemap)
m.to_streamlit(height=350)

# Crop Picture _______________________________________________________________________
if coordinates != "":
    image_map = utils.save_crop_image(m,top_left_coordinates, bottom_right_coordinates) 
    st.write("")
    st.write("")
    col1, col2, col3 = st.columns(3)
# ___________________________________________________________________________________
    img_byte_arr = io.BytesIO()
    image_map.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    list_file_png = [img_byte_arr]

    if list_file_png:
        # Collect bytes
        # files_bytes = [file.read() for file in list_file_png]
        # Apply model
        probas = classif_silo(list_file_png, classif_model)

        # Plotting the proportion of images having silos
        n_pic_silos = np.sum(probas>.5)
        n_pic_no_silos = np.sum(probas<=.5)
        data_bar_chart = pd.DataFrame({
            "Type": ["Silo found", "No silo found"], 
            "Number" : [n_pic_silos, n_pic_no_silos]
        })
        col1, col2, col3 = st.columns(3)

        idx_silos = 0
        
        for idx, file_pgn in enumerate(list_file_png):
            segmented_image = segment_silo(file_pgn, segment_model)
                    
    
    with col1:
        st.markdown("<h5 style='text-align: center; color: midnightblue;'>Cropped image</h5>", unsafe_allow_html=True)
        st.image(image_map)

    with col2:
        st.markdown("<h5 style='text-align: center; color: midnightblue;'>Bar Chart</h5>", unsafe_allow_html=True)
        st.bar_chart(data_bar_chart, x="Type", y="Number", width=200, use_container_width=False)
    
    with col3:
        st.markdown("<h5 style='text-align: center; color: midnightblue;'>Segmented image</h5>", unsafe_allow_html=True)
        st.image(segmented_image, clamp=True)
