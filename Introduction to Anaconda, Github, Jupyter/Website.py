import streamlit as st
from PIL import Image
import os
from pathlib import Path

# Set forced white background
st.set_page_config(layout="wide")

# Helper function to get correct image paths
def get_image_path(image_name):
    base_path = Path(__file__).parent
    pictures_path = base_path / "Pictures"
    return str(pictures_path / image_name)

# Sidebar navigation
st.sidebar.title("Navigation")
selected_guide = st.sidebar.selectbox(
    "Select Guide",
    ["Anaconda Navigator", "Jupyter Lab", "GitHub Desktop", "Visual Studio Code"],
    index=0  # Default to Anaconda Navigator
)

# The content for each guide is removed, leaving a blank page for now.
# You can add new content here based on the selected_guide variable.
if selected_guide == "Anaconda Navigator":
    st.markdown("<h1 style='color:orange;'>Anaconda Navigator</h1>", unsafe_allow_html=True)
    st.image(get_image_path("anaconda_icon.jpeg"), width=596)
    st.image(get_image_path("anaconda_main_menu.png"), width=595)
    st.write("") # Adds a blank line for spacing
    st.markdown("""
    Anaconda Navigator is a **graphical user interface (GUI)** that simplifies the use of Python for environment management and data science. It comes with the Python language when installed, however it also allows for ease of "Virtual Environments" management unlike the individual Python.

    - **Installation:** Go to https://www.anaconda.com/download and either "skip registration" or sign in with your Google accounted, after that choose the correct version (for Mac or Windows operating system) and download. Open up the installer, *keeping the default settings (except file path if you want to change where you want to install)* and finish.
    - **Getting started:** When first opened, the menu (as shown above) will pop up showing a range of apps, some already come with anaconda while other have to installed. Unlike normal, apps opened through Anaconda *will use Anaconda Environments automatically.*
    - **Virtual Environments (VE):** In the "Environments" tab, you should see "base (root)", this is an environment already installed with Anaconda, it is already packaged with prominent Python Packages. You can create new VE and use those VE instead. Each VE packages will independent from each other enabling you to use different set of packages for different projects.

    => In short, Anaconda provides an easier management of tools for a different range of projects. For the students, it mainly helped ease out the process of downloading tools for the lectures and ensuring that the students have access the tools for their lectures.

    For more detailed instructions:
    Visit https://www.anaconda.com/docs/tools/anaconda-navigator/getting-started.
    """)


elif selected_guide == "Jupyter Lab":
    st.markdown("<h1 style='color:orange;'>Jupyter Lab guide</h1>", unsafe_allow_html=True)
    st.write("Content for Jupyter Lab will go here.")

elif selected_guide == "GitHub Desktop":
    st.markdown("<h1 style='color:orange;'>GitHub Desktop</h1>", unsafe_allow_html=True)
    st.write("Content for GitHub Desktop will go here.")

elif selected_guide == "Visual Studio Code":
    st.markdown("<h1 style='color:orange;'>Visual Studio Code</h1>", unsafe_allow_html=True)
    st.write("Content for Visual Studio Code will go here.")
