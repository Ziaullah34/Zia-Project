from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain


# Directories and the file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "styles" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "car_animation.json"

# Function to display lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Apply Effect for Snow Animation
def run_snow_animation():
    rain(emoji="❄️", font_size=18, falling_speed=4, animation_length="infinite")

# Function to get the name
def getting_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Mate"])[0]

# Page Configuration
st.set_page_config(page_title="Happy Journey", page_icon="😍")

# Running the snow animation
run_snow_animation()

# Applying CSS files
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Personalized name
PERSON_NAME = getting_person_name()
st.header(f"Happy Journey, {PERSON_NAME}! 🚗")

# Displaying the animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=320)

# Personal Message
st.markdown(f"Dear {PERSON_NAME}! I wish a great trip to you and your family")
