import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from utils.add_logo import add_logo

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Foodix-Silo-Detection", page_icon=":corn:", layout="wide")  
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

# Functions __________________________________________________________________________
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_4lyswkde.json")
img_silos_satelite = Image.open("images/silos_satelite.png")
img_silos_segmentation = Image.open("images/silos_segmentation.png")

# ---- HEADER SECTION ----
with st.container():
    st.title("Foodix")
    st.subheader("Diminish global famine crisis making cereals available for all families and communities across the globe")
    st.write(
        '''
            ______________________________________________________________________________
            ______________________________________________________________________________
            ______________________________________________________________________________
        '''
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who we are and what we do:")
        st.write("##")
        st.write(
            """
            About McKinsey:
            - Our experience includes agriculture __________________________
            - 5000 Consultants only in Idao 
      
            If this sounds interesting to you, consider hiring us for your project.
            """
        )
        st.write("[Our Website >](https://www.mckinsey.com/)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Our Data Projects:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_silos_satelite)
    with text_column:
        st.subheader("Classification of Silos from Satelite images")
        st.write(
            """
                ______________________________________________________________________________
                ______________________________________________________________________________
                ______________________________________________________________________________
            """
        )
        st.markdown("[See model results...](http://localhost:8501/Classification_model)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_silos_segmentation)
    with text_column:
        st.subheader("Picture Segmentation and exact localization of silos")
        st.write(
            """
                ______________________________________________________________________________
                ______________________________________________________________________________
                ______________________________________________________________________________
            """
        )
        st.markdown("[See model results...](http://localhost:8501/Segmentation_model)")

