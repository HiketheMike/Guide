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
    st.image(get_image_path("anaconda_icon.jpg"), width=596)
    st.image(get_image_path("anaconda_menu.png"), width=595)
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
    st.markdown("<h1 style='color:orange;'>Visual Studio Code and Jupyter Notebooks</h1>", unsafe_allow_html=True)

    # VSC logo (centered)
    col1, col2, col3 = st.columns([1, 2, 1]) # Use columns to help center the image
    with col1:
        st.image(get_image_path("VSC_icon.jpg"), width=300)
    st.write("") # Add a blank line for spacing

    st.markdown("""
    Visual Studio Code is an Integrated Development Environment (IDE) that allows us to use many programming languages (e.g R, Python, C++,...). It comes with many extensions that allows for flexibility and versatility, one of these extensions include the "Jupyter" extension, which allows you to read and write with Jupyter Notebook files (.ipynb files).

    - **Installation:** Go to https://code.visualstudio.com/download, and download the version suitable with your device operating system.

    - **Setting up Jupyter and Python extension:** Following the VSC interface above...

    1.  Go to Activity Bar and find **Extensions**.
    2.  In the **Extensions** tab, there is a search bar, type "Jupyter" and click on "Jupyter" in search results, you will be asked to install the extension. Repeat this step for the "Python" extension. After that, clear the search bar, and make sure that Jupyter/ Python and its extra components are installed (for reference, look at **Required extensions**).

    - **Opening a Jupyter Notebook:** After that, go to the activity bar and look for **Explorer**, in here there are 3 options for you to open a Jupyter notebook file...  
        1.  Right-click --> "Add Folder to workspace": allows you to choose the folder that contain the Jupyter notebook file and read it. However unlike opening individual files, this functions allows you to *access other dependencies* such as pictures and videos that are embeded to a local notebook. If you open a notebook and see some missing pictures, then you would need to use this function instead.
        2.  Right-click --> New File --> Jupyter Notebook: allows you to make a new notebook and use it.

    - **Running a Jupyter Notebook:** A Jupyter notebook allows you to *write codes* and *plain texts*, to run code cell...
        1.  Click on a cell and press the "Run" button. If you want to run the entire notebook, look on top of the **Editor** there should be a "Run all" button.
        2.  A prompt pops up *on top,* assuming you used **Anaconda Navigator** to open VSC, choose Select a Kernel --> Python Environments --> base (python x.xx.x). It will then proceed to run the codes.
        3.  If finished and without any errors, an output would be put below the code cells. Markdown text cells would become plain text cells once run instead.

    => With Visual Studio Code, we can run Notebooks that contain codes that can be used to create graphs or simulations that the lecturer creates which helps create a more dynamic studying activities. Moreover, the use to Markdown text cells allows for explanations and formulas alongside the code outputs.
    """)

