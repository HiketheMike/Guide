import streamlit as st
from PIL import Image
import os
from pathlib import Path

# Set page config
st.set_page_config(layout="wide")

# Helper function to get correct image paths
def get_image_path(image_name):
    base_path = Path(__file__).parent
    pictures_path = base_path / "Pictures"
    return str(pictures_path / image_name)

# --- Title and Introduction ---
st.markdown("<h1 style='color:orange;'>Anaconda Navigator</h1>", unsafe_allow_html=True)

# Load Anaconda logo
try:
    st.image(get_image_path("Anaconda logo.jpg"), caption="Anaconda Logo", width=500)
except FileNotFoundError:
    st.warning("Anaconda logo image not found. Please ensure the image file exists.")
    
st.write("- To have access to Data science tools in just 1 download (contains Python, and some other applications)")

# --- Anaconda Navigator Installation ---
st.markdown("<a name='anaconda-navigator-installation'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='color:red;'>Anaconda Navigator Installation</h2>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("## **Step 1:**")
    st.write("- Go to [Anaconda Navigator](https://www.anaconda.com/products/navigator)")
    st.write("- Press **Download Now**")
    st.write("- **Skip registration** for email for now.")

with st.container(border=True):
    st.markdown("## **Step 2: Choose a suitable version for your Device**")
    st.write("- Go to **Distribution Installers** not **Miniconda Installers** and choose a suitable version.")
    st.write("- Check the guide below to find your suitable version.")
    
    # Load Anaconda versions image
    try:
        st.image(get_image_path("Anaconda_versions.png"), 
                caption="Anaconda Versions Guide", width=700)
    except FileNotFoundError:
        st.warning("Anaconda versions image not found.")

    st.markdown("### 🪟 *Windows Guide*")
    st.write("- For Windows, we only need to click on either the **Default installation** or the **64-Bit Graphical Installer (912.3M)** to download.")

    st.markdown("### 🍎*MacOS Guide*")
    st.write("- You will be asked to download either **Intel** or **Apple Silicon**. The installation of this depends on whether your Mac is running on an INTEL or M1/M2/M3 chip. Here are the steps for you to check:")
    st.write("   - Click on the **Apple icon** on the top left of your screen and go to **About This Mac** and look for **Chip**:")
    st.markdown("     - If you see: `Apple M1`, `M2`, or `M3` --> **Download Apple Silicon** OR **64-Bit (Apple silicon) Graphical Installer (704.7M)**")
    st.markdown("     - If you see: `Intel Core i5`, `i7`, etc. --> **Download Intel** OR **64-Bit (Intel chip) Graphical Installer (734.7M)**")
    st.write("- Don't DOWNLOAD **64-Bit (Apple silicon) Command Line Installer (707.3M)** OR **64-Bit (Intel chip) Command Line Installer (731.2M)** as they require you to use the command prompt to download them properly.")

    st.markdown("### 🐧 *Linux Guide*")
    st.write("- For linux, open up your **terminal**, and type `uname -p`, and you will see the current Linux Architecture you are using. For the corresponding Architecture, you would run the one of the following command lines:")
    st.code("curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-aarch64.sh", language="bash")
    st.code("curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh", language="bash")
    st.code("curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-s390x.sh", language="bash")
    st.write("- After that, run One of the following commands following your architecture:")
    st.code("bash ~/Anaconda3-2024.10-1-Linux-aarch64.sh", language="bash")
    st.code("bash ~/Anaconda3-2024.10-1-Linux-x86_64.sh", language="bash")
    st.code("bash ~/Anaconda3-2024.10-1-Linux-s390x.sh", language="bash")
    st.write("- Press **Enter** and after that type `yes`.")
    st.write("- Next it would show you the directory being downloaded to, press **Enter** to finish the download.")
    st.write("- Finally, it will ask you if you want to activate conda's base environment everytime you open up the terminal, Type `yes` as it will make it easier for you to run anaconda commands. After that restart your terminal.")
    st.write("- Type `anaconda-navigator` from their terminal to Open up **Anaconda Navigator**.")
    st.write("> => Once it is downloaded, run the installer.")

with st.container(border=True):
    st.markdown("## **Step 3: Finishing Installation**")
    st.write("- For both Mac and Windows, the **default options** are sufficient and should not be changed, just click continue and proceed with the installation.")
    st.write("- Open up **Anaconda Navigator**.")

# --- Video Guide ---
st.markdown("<a name='video-guide-(from-the-official-anaconda-website)'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='color:red;'>Video Guide (from the Official Anaconda website)</h2>", unsafe_allow_html=True)

# Using the exact YouTube video IDs from your markdown
st.write("### FOR WINDOWS")
st.video("https://www.youtube.com/watch?v=yFeVEAeOcnE")

st.write("### FOR MACOS")
st.video("https://www.youtube.com/watch?v=DNu8pQOYRGg")

st.write("### For LINUX")
st.video("https://www.youtube.com/watch?v=sU2mXjOB-fA")

st.success("✅ **Anaconda Navigator** is now Ready to be used. You now have access to all the essential tools for the course. There are also video guide below from the Official Anaconda Website.")

# --- Getting Used to Anaconda ---
st.markdown("<a name='getting-used-to-anaconda'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='color:red;'>Getting used to Anaconda</h2>", unsafe_allow_html=True)

st.markdown("### <span style='color:blue;'> 1. Main Interface Overview</span>", unsafe_allow_html=True)
with st.container(border=True):
    try:
        st.image(get_image_path("Anaconda_Navigator.png"), 
                caption="Anaconda Navigator Main Interface", width=700)
    except FileNotFoundError:
        st.warning("Anaconda navigator interface image not found.")

    st.markdown("""
    | Component   | Description                     |
    |-------------|---------------------------------|
    | Home        | Launch applications like Jupyter, Spyder, etc. |
    | Environments| Manage Conda environments       |
    | Learning    | Tutorials and documentation     |
    | Community   | Anaconda community resources    |
    """)

st.markdown("### <span style='color:blue;'> 2. Managing Environments</span>", unsafe_allow_html=True)
with st.container(border=True):
    try:
        st.image(get_image_path("Anaconda_environments.png"), 
                caption="Anaconda Environments Management", width=700)
    except FileNotFoundError:
        st.warning("Anaconda environments image not found.")

    st.markdown("""
    *Default Environment (`base`)*
    - The default base environment (~560 packages) is pre-installed with Anaconda.
    - Apps launched from Anaconda use `base` by default.
    """)
    st.markdown("""
    *Why Use Separate Environments?*
    - **Isolation**: Environments act like independent "baskets" for packages—errors in one won't affect others.
    - **Safety**: If an environment breaks, delete it and create a new one without reinstalling everything.
    """)
    st.markdown("""
    *Switching Environments*
    1. Select your desired environment (e.g., `apex`) from the dropdown.
    2. Launch apps (Jupyter, Spyder, etc.)—they'll now use the selected environment.
    """)
    st.markdown("""
    *Environments customization*
    - **Create** new environments
    - **Clone/Remove** existing ones
    - **Import/Export** environments
    """)
    st.write("*(See screenshot for visual guide.)*")

st.markdown("### <span style='color:blue;'> 3. Installing Packages</span>", unsafe_allow_html=True)
with st.container(border=True):
    st.write("- Most packages come pre-installed in the **base** environment")
    st.write("- To add new packages in any environment, write this command:")
    st.code("%pip install <package>")
    st.write("(Works in Jupyter Lab or VS Code **code** cells, as shown below)")