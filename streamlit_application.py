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
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        st.warning("Lottie animation file not found.")
        return None

# Apply Snow Animation
def run_snow_animation():
    rain(emoji="❄️", font_size=18, falling_speed=4, animation_length="infinite")

# Function to get the name from query parameters
def getting_person_name():
    query_params = st.experimental_get_query_params()  # Only use experimental if necessary
    return query_params.get("name", ["Mate"])[0]

# Page Configuration
st.set_page_config(page_title="Happy Journey", page_icon="😍")

# Run Snow Animation
run_snow_animation()

# Apply CSS
apply_css()

# Personalized name
PERSON_NAME = getting_person_name()
st.header(f"Happy Journey, {PERSON_NAME}! 🚗")
st.markdown(f"Dear {PERSON_NAME}! I wish a great trip to you and your family.")


