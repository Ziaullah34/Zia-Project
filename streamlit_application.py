from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
BASE_DIR = Path(__file__).parent
CSS_FILE = BASE_DIR / "style.css"
LOTTIE_ANIMATION = BASE_DIR / "car_animation.json"

# Apply CSS if the file exists
def apply_css():
    if CSS_FILE.exists():
        with open(CSS_FILE) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to display lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Apply Effect for Snow Animation
def run_snow_animation():
    rain(emoji="❄️", font_size=18, falling_speed=4, animation_length="infinite")

# Function to get the name
def getting_person_name():
    query_params = st.experimental_get_query_params()  # Corrected method
    return query_params.get("name", ["Mate"])[0]  # Default to 'Mate' if no name is passed

# Page Configuration
st.set_page_config(page_title="Happy Journey", page_icon="😍")

# Running the snow animation
run_snow_animation()

# Applying CSS files
apply_css()

# Personalized name
PERSON_NAME = getting_person_name()
st.header(f"Happy Journey, {PERSON_NAME}! 🚗")

# Load Lottie animation and display it
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, speed=1, width=700, height=400)
