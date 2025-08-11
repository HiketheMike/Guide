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
    ["Anaconda Navigator", "Visual Studio Code and Jupyter Notebooks", "GitHub Desktop"],
    index=0  # Default to Anaconda Navigator
)

# The content for each guide is removed, leaving a blank page for now.
# You can add new content here based on the selected_guide variable.
if selected_guide == "Anaconda Navigator":
    st.markdown("<h1 style='color:orange;'>Anaconda Navigator</h1>", unsafe_allow_html=True)
    # Use columns to center the image and its caption
    col_left, col_right = st.columns(2)
    with col_left:
        st.image(get_image_path("anaconda_menu.png"), width=500)
        st.markdown("<div style='text-align: center;'>Anaconda Home Menu</div>", unsafe_allow_html=True)
    with col_right:
        st.image(get_image_path("anaconda_environments.png"), width=500)
        st.markdown("<div style='text-align: center;'> Anaconda Environments tab</div>", unsafe_allow_html=True)
    st.write("") 
    st.write("")

    st.write("") # Adds a blank line for spacing
    st.markdown("""
    Anaconda Navigator is a **graphical user interface (GUI)** that simplifies the use of Python for environment management and data science. It comes with the Python language when installed, however it also allows for ease of "Virtual Environments" management unlike the individual Python.
    """)
    st.markdown("""
    - **Installation:** Go to https://www.anaconda.com/download and either "skip registration" or sign in with your Google accounted, after that choose the correct version (for Mac or Windows operating system) and download. Open up the installer, *keeping the default settings (except file path if you want to change where you want to install)* and finish.
    """)
    st.markdown("""
    - **Getting started:** When first opened, the menu (as shown above) will pop up showing a range of apps, some already come with anaconda while other have to installed. Unlike normal, apps opened through Anaconda *will use Anaconda Environments automatically.*
    """)
    st.markdown("""
    - **Virtual Environments (VE):** In the "Environments" tab, you should see "base (root)", this is an environment already installed with Anaconda, it is already packaged with prominent Python Packages. You can create new VE and use those VE instead. Each VE packages will independent from each other enabling you to use different set of packages for different projects.
    """)
    st.markdown("""
    => In short, Anaconda provides an easier management of tools for a different range of projects. For the students, it mainly helped ease out the process of downloading tools for the lectures and ensuring that the students have access the tools for their lectures.
    """)
    st.markdown("""
    For more detailed instructions:
    Visit https://www.anaconda.com/docs/tools/anaconda-navigator/getting-started.
    """)


elif selected_guide == "Visual Studio Code and Jupyter Notebooks":
    st.markdown("<h1 style='color:orange;'>Visual Studio Code and Jupyter Notebooks</h1>", unsafe_allow_html=True)


    # VSC Interface and Required extensions (side-by-side)
    col_left, col_right = st.columns(2)
    with col_left:
        st.image(get_image_path("VSC_interface.png"), width=500)
        st.markdown("<div style='text-align: center;'>VSC Interface</div>", unsafe_allow_html=True)
    with col_right:
        st.image(get_image_path("VSC_extensions.png"), width=500)
        st.markdown("<div style='text-align: center;'> Required extensions (left panel, 8 extensions are seen)</div>", unsafe_allow_html=True)
    st.write("") 
    st.write("")
    
    st.markdown("""
    Visual Studio Code is an Integrated Development Environment (IDE) that allows us to use many programming languages (e.g R, Python, C++,...). It comes with many extensions that allows for flexibility and versatility, one of these extensions include the "Jupyter" extension, which allows you to read and write with Jupyter Notebook files (e.g file_name.ipynb).
    """)

    st.markdown("""
    - **Installation:** Go to https://code.visualstudio.com/download, and download the version suitable with your device operating system.
    """)
                
    st.markdown("""
    - **Setting up Jupyter and Python extension:** Following the VSC interface above...

        1.  Go to Activity Bar and find **Extensions**.
        2.  In the **Extensions** tab, there is a search bar, type "Jupyter" and click on "Jupyter" in search results, you will be asked to install the extension. Repeat this step for the "Python" extension. After that, clear the search bar, and make sure that Jupyter/ Python and its extra components are installed (for reference, look at **Required extensions**).
    """)
                
    st.markdown("""
    - **Opening a Jupyter Notebook:** After that, go to the activity bar and look for **Explorer**, in here there are 2 options for you to open a Jupyter notebook file...  
        1.  File --> Add Folder to workspace: allows you to choose the folder that contain the Jupyter notebook file and read it. However unlike opening individual files, this functions allows you to *access other dependencies* such as pictures and videos that are embeded to a local notebook. If you open a notebook and see some missing pictures, then you would need to use this function instead.
        2.  File --> New File --> Jupyter Notebook: allows you to make a new notebook and use it.
    """)
                
    st.markdown("""
    - **Running a Jupyter Notebook:** A Jupyter notebook allows you to *write codes* and *plain texts*, to run code cell...
        1.  Click on a cell and press the "Run" button. If you want to run the entire notebook, look on top of the **Editor** there should be a "Run all" button.
        2.  A prompt pops up *on top,* assuming you used **Anaconda Navigator** to open VSC, choose Select a Kernel --> Python Environments --> base (python x.xx.x). It will then proceed to run the codes. (If you don't open VSC with Anaconda, then you would have to use your own separate python language)
        3.  If finished and without any errors, an output would be put below the code cells. Markdown text cells would become plain text cells once run instead.
    """)

    st.markdown("""
    => With Visual Studio Code, we can run Notebooks that contain codes that can be used to create graphs or simulations that the lecturer creates which helps create a more dynamic studying activities. Moreover, the use to Markdown text cells allows for explanations and formulas alongside the code outputs.
    """)

    st.markdown(""" For more detailed instructions: Visit https://code.visualstudio.com/docs """)

elif selected_guide == "GitHub Desktop":
    st.markdown("<h1 style='color:orange;'>GitHub Desktop</h1>", unsafe_allow_html=True)
    

    # GitHub starting interface image (centered)
    col1, col2, col3 = st.columns([1, 2, 1]) # Adjust ratios as needed for centering
    with col2:
        st.image(get_image_path("GitHub_interface.png"), width=563)
        st.markdown("<div style='text-align: center;'>GitHub starting interface</div>", unsafe_allow_html=True)
    st.write("") # Adds a blank line for spacing
    
    # New images aligned left and right
    col_left_gh, col_right_gh = st.columns(2)
    with col_left_gh:
        st.image(get_image_path("GitHub_functions.png"), width=544)
        st.markdown("<div style='text-align: center;'>The various functions of GitHub Desktop</div>", unsafe_allow_html=True)
    with col_right_gh:
        st.image(get_image_path("GitHub_pull.png"), width=545)
        st.markdown("<div style='text-align: center;'>An example of Pulling</div>", unsafe_allow_html=True)
    st.write("") # Add a blank line for spacing

    st.markdown("""
    - **Installation:** Go to https://desktop.github.com/download/, and download the suitable version for your device. After finishing the installation, you will be prompted to create a GitHub account, you can skip this if you want and do it later.
    """)
    
    st.markdown("""
    - **Cloning (Download from online repository):**
        1.  When first starting GitHub Desktop, you have 3 main options, to pull choose **Clone a repository from the Internet** --> **URL**.
        2.  Later, after download from 1 repository, you can download another different repository by clicking on **File** --> **Clone repository** --> **URL**.

    You would then need the **URL** to the remote repository as well as the **filepath** to the folder where you want to store the files. The URL can be found as in this example:
    """)


    st.write("") # Adds a blank line for spacing
    # Use columns to center the video and its caption
    col1, col2, col3 = st.columns([1, 2, 1]) # Adjust ratios as needed for centering
    with col2:
        st.video("https://youtu.be/U9AVfBaTKZs") # Use the YouTube URL directly
        st.markdown("<div style='text-align: center;'>Guide on collecting URL for GitHub Repositories</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    **Note**: It is common, that after you clone the files, you would proceed make a copy of the files elsewhere and add modifications in the copied files. This would reduce conflict between the version of that is modified by you and the owner of the repo and prevent potential issues.
    """)
    
    st.write("") # Adds a blank line for spacing
    st.markdown("""
    - **Fetching and Pulling (Update from online repository):** Once you have a cloned repo, it is possible that the owner of the repo updated some files, in that case we would use the Fetch button and 2 things will happen:
        1.  You pressed the **Fetch Origin** button on top and nothing happens, this means that the files are up-to-date.
        2.  You pressed the **Fetch Origin** button and it becomes **Pull Origin** (shown on the picture above), this means that there are updates to the local files. If you get this prompt, pressed **Pull Origin**, and go to where you stored your local folder, changes will be made there.
    """)


    st.markdown("""
    - **Pushing (Update TO Online Repository)*:** Given that you have made a GitHub account and decided to open a repository, you can choose the create a local folder and Push it to a Remote Repository. Since this guide mainly focus on accessing the tools, it is recomended that the reader learn about it in other sources.
                """)

    st.markdown("""=> GitHub is mainly a tool for storing files. As projects or courses progress. There will be updates to the remote folder by the user, so make sure to fetch origin often to stay updated.""")

    st.markdown(""" For more detailed instructions: Visit https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop """)