import streamlit as st
import utils
import plotly.figure_factory as ff
import numpy as np
import io
from PIL import Image
import leafmap.foliumap as leafmap
import os 
import cv2
from utils.add_logo import add_logo

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Foodix-Coordinates", page_icon=":corn:", layout="wide")
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

    with col1:
        st.write(' ')

    with col2:
         st.markdown("<h5 style='text-align: center; color: darkgreen;'>Cropped image</h5>", unsafe_allow_html=True)
         st.image(image_map)
    
    with col3:
        st.write(' ')
        

   