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


if selected_guide == "Anaconda Navigator":
    # --- ANACONDA NAVIGATOR GUIDE CONTENT ---
    # --- Title and Introduction ---
    st.markdown("<h1 style='color:orange;'>Anaconda Navigator</h1>", unsafe_allow_html=True)

    # Load Anaconda logo
    try:
        st.image(get_image_path("Anaconda logo.jpg"), caption="Anaconda Logo", width=500)
    except FileNotFoundError:
        st.warning("Anaconda logo image not found. Please ensure the image file exists.")
        
    
    st.write("**Anaconda Navigator** is your go-to desktop graphical user interface (GUI) for efficient data science and machine learning.")
    st.write("""
    - **Streamlined Workflow Management:** Designed to simplify the execution and oversight of your data science and ML projects.
    - **Unified Application Portal:** Provides one-click access to critical tools like **Jupyter Notebook**, **Spyder**.
    - **Comprehensive Environment & Package Management:** Ensures a consistent, version-controlled development environment.
    - **Simplified Setup:** A single download eliminates complex installations, getting you productive faster.
    """)

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
            st.image(get_image_path("Anaconda_navigator.png"), 
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

elif selected_guide == "Jupyter Lab":
    st.markdown("<h1 style='color:orange;'>Jupyter Lab guide</h1>", unsafe_allow_html=True)
    
    st.write("- With the **base(root)** environment chosen navigate to the **Home** section in Anaconda Navigator.")
    st.write("- Open up **Jupyter Lab**, it should have been automatically installed already, if its not then you're choosing the **wrong environment**.")
    
    st.markdown("<h2 style='color:red;'>Main Overview</h2>", unsafe_allow_html=True)
    st.write("When opening up Jupyter Lab, Select **Python 3(ipykernel)** in the **Notebook** section, this should give make a new Jupyter Notebook file.")
    st.write("Jupyter supports 3 cell types for mixed code and documentation:")
    st.write("1. **Code Cells** - For executable code")
    st.write("2. **Markdown Cells** - For formatted text/explanations")
    st.write("3. **Raw Cells** - Unformatted plain text (rarely used)")
    st.write("- Switch between types using the dropdown in the toolbar, it will change the current cell type.")

    try:
        st.image(get_image_path("Cell_types.png"), width=1000)
    except FileNotFoundError:
        st.warning("Cell_types.png not found")

    st.write("Some useful shortcuts for cell actions in **Command mode**, you can quit **Edit Mode** by pressing **Esc**:")
    st.markdown("""
    | Action                        | Shortcut                     |
    | ----------------------------- | ---------------------------- |
    | Run cell (stay in cell)       | `Ctrl/Cmd + Enter`           |
    | Add cell below                | `B`                          |
    | Add cell above                | `A`                          |
    | Delete selected cell          | `D` then `D` (press D twice) |
    | Copy cell                     | `C`                          |
    | Cut cell                      | `X`                          |
    | Paste cell below              | `V`                          |
    | Paste cell above              | `Shift + V`                  |
    | Change to Markdown cell       | `M`                          |
    | Change to Code cell           | `Y`                          |
    | Saving the file               | `Ctrl/Cmd + S`               |
    """)

    st.markdown("<h3 style='color:blue;'>Markdown/Raw Cells</h3>", unsafe_allow_html=True)
    st.write("*Markdown Cells*")
    st.write("- Function like **Microsoft Word** - supports text formatting, images, and videos")
    st.write("- **Not** interpreted as code (unlike code cells)")
    st.write("- It also enables some formatting (you can copy these these formats and try it yourself):")
    
    st.code(
    """
    <span style='color:red'>Colored text</span>
    <div style='border:2px solid black; padding:10px'>Bordered box</div>
    <div class='alert alert-info'>Info alert box</div>
    """, language='python')
    
    st.write("*Raw Cells*")
    st.write("- Plain text **without any formatting**")
    st.write("- Rarely used due to limited functionality")
    st.write("> Markdown streamlines documentation by combining formatted text with executable code.")

    st.markdown("<h3 style='color:blue;'>Code cells</h3>", unsafe_allow_html=True)
    st.code("""# In code cells, we can put a "#" to denote a "comment"
# Any text written here is considered plain text, this helps to explain a chunk of code

# Here's a simple math function
a = 5 + 1
print(f'Result: {a}')
# You can also download packages using code cells
%pip install yfinance
""", language="python")

    st.markdown("<h2 style='color:red;'>Creating and exporting a Notebook on Lab</h2>", unsafe_allow_html=True)
    st.write("- To start with a new Notebook, Go to **File** and choose **New** then **Notebook**. Now you would be able to write your own work into this file.")
    
    try:
        st.image(get_image_path("Jupyter_new_file.png"), width=350)
    except FileNotFoundError:
        st.warning("Jupyter_new_file.png not found")

    st.write("- Below in the picture, you can also see the option **Save and Export Notebook As** — click on it and choose **HTML**.")

    st.markdown("<h2 style='color:red;'>Accessing Folders</h2>", unsafe_allow_html=True)
    st.write("- Click the **Folders** icon (left sidebar) to view files")
    st.write("- Jupyter only accesses files within its **current working directory**")
    st.write("- If you're file isn't in this directory, you cannot access it through Jupyter Lab.")
    st.write("> See guide below to check your current directory")

    try:
        st.image(get_image_path("Jupyter_folder.png"), width=350)
    except FileNotFoundError:
        st.warning("Jupyter_folder.png not found")

    st.markdown("<h2 style='color:red;'>Checking the current working directory</h2>", unsafe_allow_html=True)
    st.write("On YOUR **Jupyter lab** Code cell write this function:")
    st.code("""import os
os.getcwd() 

# Example Output (Your output should look like this)
'C:\\Users\\LENOVO\\'
""", language="python")

    st.write("- It will Output the **Directory** that Jupyter is connecting to,  **copy that Directory Path** as it will be used later for Github Desktop.")

elif selected_guide == "GitHub Desktop":
    # --- GITHUB DESKTOP GUIDE CONTENT ---
    st.markdown("<h1 style='color:orange;'>GitHub Desktop</h1>", unsafe_allow_html=True)
    
    try:
        st.image(get_image_path("Github_desktop.png"), width=500)
    except FileNotFoundError:
        st.warning("Github_desktop.png not found")
    
    # --- Installation ---
    st.markdown("<h2 style='color:red;'>GitHub Desktop Installation</h2>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("## **Step 1: Download GitHub Desktop**")
        st.write("- Go to [Github Desktop](https://desktop.github.com/download/)")
        
        try:
            st.image(get_image_path("Github_download.png"), width=850)
        except FileNotFoundError:
            st.warning("Github_download.png not found")
        
        st.markdown("### 🪟🍎 *Windows Guide and MacOS Guide*")
        st.write("- For Windows, we only need to click on either the **Default installation** or the **64-Bit Graphical Installer (912.3M)** to download.")
        st.write("- Downloading GitHub is more straightforward, for your corresponding system, click on either **Download for Windows (64-bit)** or **download for macOS**.")
        st.write("- Once it is downloaded, run the installer.")
        st.write("> => Once it is downloaded, run the installer.")
    
    with st.container(border=True):
        st.markdown("### 🐧 *Linux Guide*")
        st.write("- For linux users, go to this website https://github.com/shiftkey/desktop, it will take you to a github repository.")
        st.write("- Choose the correct version of your Linux system and download it.")
        st.write("- Navigate to where you downloaded the file and right click, choose **Open Terminal in here**.")
        st.write("- Use the command `sudo apt install ./<file>` or `sudo dpkg -i <file>`.")
    
    st.video("https://www.youtube.com/watch?v=Foqs70mT2yc")
    
    with st.container(border=True):
        st.markdown("## **Step 2: Install GitHub Desktop**")
        st.write("- Wait for it to **Install**")
        st.write("- After opening GitHub, it would ask you to link with your **GitHub account** as well as **Configure Git**, **skip this step** and press **finish**, you can login later.")
    
    # --- Cloning Repository ---
    st.markdown("<h2 style='color:red;'>Cloning a github repository downloading data from github</h2>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("## **Step 1: Obtain the URL**")
        st.write("- First, go to [GitHub website](https://github.com/) and search for the name **DROCLB** and look into the **Users** section.")
        
        try:
            st.image(get_image_path("Cloning_1.png"), width=750)
        except FileNotFoundError:
            st.warning("Cloning_1.png not found")
        
        st.write("- Now go to the **Repositories** section and look for **Financial_Tools** repository, click on it.")
        
        try:
            st.image(get_image_path("Cloning_2.png"), width=750)
        except FileNotFoundError:
            st.warning("Cloning_2.png not found")
        
        st.write("- **Get the HTTPS link**")
        st.write("  - Click the `<> Code` button")
        st.write("  - Copy the provided URL")
        
        try:
            st.image(get_image_path("Github_url.png"), width=750)
        except FileNotFoundError:
            st.warning("Github_url.png not found")
        
        st.write("- It's a good practice to know where to get the files, you can however quickly access the link by clicking here" \
        " https://github.com/DROCLB/Financial_Tools.git")
    
    with st.container(border=True):
        st.markdown("## **Step 2: Putting it all together**")
        st.write("1. **Paste the HTTPS URL** (copied from GitHub)")
        st.write("2. **Set the Local Path** to your Jupyter Lab directory")
        st.write("   - The folder name (e.g., `Codes`) can be modified")
        st.write("> Note: Ensure the path matches Jupyter's working directory.")
        
        try:
            st.image(get_image_path("Cloning_6.png"), width=500)
        except FileNotFoundError:
            st.warning("Cloning_6.png not found")
        
        st.write("- It will Clone the GitHub Repository named **Codes** to your Laptop now.")
        st.write("- Now go to Jupyter lab and access the folder.")
    
    # --- Pulling Repository ---
    st.markdown("<h2 style='color:red;'>Pulling a GitHub Repository (Updating local folder)</h2>", unsafe_allow_html=True)
    st.write("*Clone vs Pull*")
    st.write("- **Clone**: Downloads entire repository (files as-is at current date)")
    st.write("- **Pull**: Updates your local copy with new changes from remote")
    st.write("*Checking for Updates*")
    st.write("1. Click **Fetch Origin** to check for remote changes")
    st.write("2. If updates exist, **Pull** to sync them locally")
    
    try:
        st.image(get_image_path("Fetch.png"), width=850)
    except FileNotFoundError:
        st.warning("Fetch.png not found")
    
    st.write("- If there **IS** any changes, then it will show up as **Pull Origin**, otherwise nothing would happen:")
    
    try:
        st.image(get_image_path("Pulling.png"), width=850)
    except FileNotFoundError:
        st.warning("Pulling.png not found")
    
    st.write("- Click on it, and your local folder will be updated.")


elif selected_guide == "Visual Studio Code":
    # --- VISUAL STUDIO CODE GUIDE CONTENT ---
    st.markdown("<h1 style='color:orange;'>Visual Studio Code</h1>", unsafe_allow_html=True)
    
    try:
        st.image(get_image_path("VSC_logo.png"), width=500)
    except FileNotFoundError:
        st.warning("VSC_logo.png not found")
    
    st.write("- As an Optional Application for your Work, you can choose to use **Jupyter Lab** in Anaconda Navigator, that should suffice.")
    st.write("- VSC applications is however, very prominent in the industry and we should know how to use it as well.")
    st.write("- VSC have all the same overview as in Jupyter lab, with little difference.")
    
    # --- Installation ---
    st.markdown("<h2 style='color:red;'>Visual Studio Code Installation</h2>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("## **Step 1: Download Visual Studio Code**")
        st.write("- Go to [Visual Studio Code](https://code.visualstudio.com/download) and choose the version for your system.")
        
        try:
            st.image(get_image_path("VSC_download.png"), width=850)
        except FileNotFoundError:
            st.warning("VSC_download.png not found")
        
        st.markdown("### 🪟 *Windows Guide*")
        st.write("- For Windows, we only need to click on either the **Default installation** or the **64-Bit Graphical Installer (912.3M)** to download.")
        
        st.markdown("### 🍎*MacOS Guide*")
        st.write("- For **Visual studio Code**, there is the **universal** installer, download it.")
        st.write("- This version is compatible for both Intel and Apple Silicon.")
        st.write("> => Once it is downloaded, run the installer.")
    
    with st.container(border=True):
        st.markdown("### 🐧 *Linux Guide*")
        st.write("- Choose the correct version of your Linux system and download it.")
        st.write("- Navigate to where you downloaded the file and right click, choose **Open Terminal in here**.")
        st.write("- Use the command `sudo apt install ./<file>` or `sudo dpkg -i <file>`.")
    
    st.video("https://www.youtube.com/watch?v=NX8SHmkuLn4")
    
    with st.container(border=True):
        st.markdown("## **Step 2: Installation**")
        st.write("- For both Mac and Windows, the **default options** are sufficient and should not be changed, just click continue and proceed with the installation")
        st.write("- Open up **Anaconda Navigator** and **Visual Studio Code** should appear as one of the installed apps across all Environments.")
        
        try:
            st.image(get_image_path("Anaconda_VSC.png"), width=850)
        except FileNotFoundError:
            st.warning("Anaconda_VSC.png not found")
        
        st.write("- And the Interface of Visual studio code should look like this:")
        
        try:
            st.image(get_image_path("VSC_startup.png"), width=850)
        except FileNotFoundError:
            st.warning("VSC_startup.png not found")
        
        st.write("- Click on the **Mark done** at the bottom to proceed.")
    
    with st.container(border=True):
        st.markdown("## **Step 3: Downloading Extensions**")
        st.write("- As we are in VSC, we need to download the **Jupyter Notebook** and **python** extension, this is required for VSC to recognize and work with Jupyter Notebook (.ipynb) files.")
        st.write("- On the top, go to **Search [Administrator]** and type `>Extensions: Install Extensions`, and there should be Extensions appear on the Left of your screen.")
        st.write("- In that tab, type **Jupyter extension** and install it if you have not installed it")
        
        try:
            st.image(get_image_path("Jupyter_extension.png"), width=850)
        except FileNotFoundError:
            st.warning("Jupyter_extension.png not found")
        
        st.write("- Do the same for the **Python extension**")
        
        try:
            st.image(get_image_path("Python_extension.png"), width=850)
        except FileNotFoundError:
            st.warning("Python_extension.png not found")
    
    # --- Creating and Exporting Notebook ---
    st.markdown("<h2 style='color:red;'>Creating and Exporting a Notebook on VSC</h2>", unsafe_allow_html=True)
    st.write("- Click on **File**, click on **New File**, and a prompt will pop up, choose **Jupyter Notebook**.")
    st.write("- To export a File, click on the **Ellipsis** here and choose **Export**.")
    
    try:
        st.image(get_image_path("Export_VSC.png"), width=750)
    except FileNotFoundError:
        st.warning("Export_VSC.png not found")
    
    st.write("- Choose **HTML**")
    
    # --- Choosing Folder ---
    st.markdown("<h2 style='color:red;'>Choosing the folder downloaded from Github Desktop</h2>", unsafe_allow_html=True)
    st.write("- In Visual Studio Code, go to the **Folders symbol** on the left hand side.")
    st.write("- Unlike **Jupyter Lab**, we need to **Choose** the folder that we need to run")
    st.write("- Choose **Open Folder** and look for the folder containing the lectures.")
    
    try:
        st.image(get_image_path("VSC_folder.png"), width=350)
    except FileNotFoundError:
        st.warning("VSC_folder.png not found")
    
    st.success("""
    **✅ Visual Studio Code is Ready!**
    You can now use **Visual Studio Code** through Anaconda Navigator
    """)