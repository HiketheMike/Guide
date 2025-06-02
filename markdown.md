<a name='jupyter-lab-guide'></a>
# <span style='color:orange'> Jupyter Lab guide </span>

- With the **base(root)** environment chosen navigate to the **Home** section in Anaconda Navigator.
- Open up **Jupyter Lab**, it should have been automatically installed already, if its not then you're choosing the **wrong environment**.
<a name='main-overview'></a>
## <span style='color:red'> Main Overview </span>

When opening up Jupyter Lab, Select **Python 3(ipykernel)** in the **Notebook** section, this should give make a new Jupyter Notebook file.

Jupyter supports 3 cell types for mixed code and documentation:

1. **Code Cells** - For executable code  
2. **Markdown Cells** - For formatted text/explanations  
3. **Raw Cells** - Unformatted plain text (rarely used)

- Switch between types using the dropdown in the toolbar, it will change the current cell type. 

<img src = '../Pictures/Cell_types.png' style='width:1000px; display:block; height:500px; margin:10px auto'>


Some useful shortcuts for cell actions in **Command mode**, you can quit **Edit Mode** by pressing **Esc**.:

| Action                        | Shortcut                     |
| ----------------------------- | ---------------------------- |
| Run cell (stay in cell)  | `Ctrl/Cmd + Enter`               |
| Add cell below          | `B`                          |
| Add cell above          | `A`                          |
| Delete selected cell   | `D` then `D` (press D twice) |
| Copy cell                | `C`                          |
| Cut cell                 | `X`                          |
| Paste cell below         | `V`                          |
| Paste cell above         | `Shift + V`                  |
| Change to Markdown cell   | `M`                          |
| Change to Code cell      | `Y`                          |
| Saving the file          | `Ctrl/Cmd + S`                    |

### <span style = 'color:blue'> Markdown/Raw Cells
<div style = 'border: 2px solid black; padding: 10px'>

*Markdown Cells*
- Function like **Microsoft Word** - supports text formatting, images, and videos
- **Not** interpreted as code (unlike code cells)
- It also enables some formatting (you can copy these these formats and try it yourself):


<span style='color:red'>Colored text</span>
<div style='border:2px solid black; padding:10px'>Bordered box</div>
<div class='alert alert-info'>Info alert box</div>


*Raw Cells*
- Plain text **without any formatting**
- Rarely used due to limited functionality

> Markdown streamlines documentation by combining formatted text with executable code.
</div>
### <span style = 'color:blue'> Code cells
# In code cells, we can put a "#" to denote a "comment"
# Any text written here is considered plain text, this helps to explain a chunk of code

# Here's a simple math function
a = 5 + 1
print(f'Result: {a}')
# You can also download packages using code cells
%pip install yfinance
<a name='creating-and-exporting-a-notebook-on-lab'></a>
## <span style='color:red'> Creating and exporting a Notebook on Lab </span>

- To start with a new Notebook, Go to **File** and choose **New** then **Notebook**. Now you would be able to write your own work into this file.  
  <img src='../Pictures/Jupyter_new_file.png' style='width:350px; display:block; height:500px; margin:10px auto'>

- Below in the picture, you can also see the option **Save and Export Notebook As** — click on it and choose **HTML**.

<a name='accessing-folders'></a>
## <span style='color:red'> Accessing Folders </span>

- Click the **Folders** icon (left sidebar) to view files
- Jupyter only accesses files within its **current working directory**
- If you're file isn't in this directory, you cannot access it through Jupyter Lab.

> See guide below to check your current directory

<img src = '../Pictures/Jupyter_folder.png' style='width:350px; display:block; height:500px; margin:10px auto'>
<a name='checking-the-current-working-directory'></a>
## <span style='color:red'> Checking the current working directory </span>


- On YOUR **Jupyter lab** Code cell write this function:
```python
import os
os.getcwd() 

# Example Output (Your output should look like this)
'C:\\Users\\LENOVO\\'
```

- It will Output the **Directory** that Jupyter is connecting to,  **copy that Directory Path** as it will be used later for Github Desktop.


</div>
<div class = 'alert alert-success'>

**Note**:
- You can now access any `.ipynb` files, 
- The next part of the guide shows how to download lectures from an online repository.