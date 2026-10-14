# pages/Poster_Page.py

import streamlit as st
from PIL import Image
import os

# --- Page configuration ---
st.set_page_config(
    page_title="Game Poster",
    page_icon="🎮",
    layout="centered"
)

# --- Page Title ---
st.title("Game Poster")

# --- Load and Display Poster Image ---
# Image should be in your repo folder: 'images/poster.png'
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "..", "images", "Poster.png")  # Relative path from pages folder

try:
    poster = Image.open(image_path)
    st.image(poster, caption="Game Poster", use_container_width=True)
except FileNotFoundError:
    st.error("Poster image not found! Please make sure 'images/poster.png' exists in the repo.")

# --- Optional Footer ---
st.markdown("---")
st.markdown("Created by: Deepak Perina | Enjoy our games! 🎉")
