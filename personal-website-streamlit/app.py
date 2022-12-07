import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Foodix-Silo-Detection", page_icon=":corn:", layout="wide")
st.sidebar.success("Select a page above.")

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
img_food = Image.open("images/danger.png")
img_food = img_food.resize((200, 200))
img_mckinsey = Image.open('images/McKinsey_Script_Mark_2019.svg.png')

# ---- HEADER SECTION ----
with st.container():
    st.title("Foodix")
    
#     st.write(
#         '''
#         • 828 million people were affected by hunger in 2021
#         
#         • The number of hungry people increased by 150 million in 2019
#         
#         • 1 human being dying from famine every 4 seconds...
# ''')

    image_column, text_column = st.columns([3, 1])
    with image_column:
        st.header("Our Mission : Diminish global famine crisis making cereals available for all families and communities across the globe")
        st.subheader(
            '''
            “The world is moving backwards in efforts to eliminate hunger and malnutrition” (FAO)
    ''')
        st.write(
            '''
            • 828 million people were affected by hunger in 2021

            • The number of hungry people increased by 150 million in 2019

            • 1 human being dying from famine every 4 seconds...
''')
    with text_column:
        st_lottie(lottie_coding, height=500, key="coding") # st.image(img_food)
    st.write("[Learn More >](https://www.fao.org/newsroom/detail/un-report-global-hunger-SOFI-2022-FAO/en)")
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.header("Who we are and what we do:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("We are 6 really cool McKinsey consultants with 20+ years of experiences")
        st.write( """
            - Our experience includes, among other things, agriculture, infrastructures, sustainability and data science
            - +700 projects carried out throughout our career
            """
        )
        st.write("##")
        st.write(
            """
            About McKinsey:
            - Our expertise includes : Strategy, Transformation, Private Equity, ...
            - +18000 consultants worldwide 
      
            If this sounds interesting to you, consider hiring us for your project.
            """
        )
        st.write("[Our Website >](https://www.mckinsey.com/)")
    with right_column:
        st.image(img_mckinsey)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header(" Zoom on one of our project: classification and segmentation of silos on satellite images")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_silos_satelite)
    with text_column:
        st.subheader("Classification of Silos from Satelite images")
        st.write(
            """
                We used deep learning methods to determine whether we could find silos within a certain zone 
            """
        )
        st.markdown("In case you're interested in our beautiful deep learning model : [see model results...](http://localhost:8501/Classification_model)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_silos_segmentation)
    with text_column:
        st.subheader("Picture Segmentation and exact localization of silos")
        st.write(
            """
                We then tried to segmentate our pictures to pinpoint the exact localization of the silos.
                
            """
        )
        st.markdown("If you want to know more about how we achieved this amazing feat : [see model results...](http://localhost:8501/Segmentation_model)")

