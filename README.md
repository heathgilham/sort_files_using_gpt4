# Sort Files Using GPT-4

## Description
Sort files into two folders depending on file content.

## Installation Instructions

### Step 1: Install Python
Before you begin, ensure you have Python installed on your system. If you do not have Python installed, follow these steps:
1. Visit the official Python website at [python.org](https://www.python.org/downloads/).
2. Download the latest version of Python for your operating system.
3. Run the installer and follow the on-screen instructions to install Python. Make sure to tick the box that says "Add Python to PATH".

### Step 2: Install Required Libraries
This project requires certain Python libraries to be installed. You can install them using the provided `install_dependencies.py` script.
1. Open the Command Prompt. You can do this by searching for "cmd" in the Windows Start menu.
2. Navigate to the root directory of this project. Use the `cd` command followed by the path to the directory. For example:

   `cd path\to\your\project`

   Replace `path\to\your\project` with the actual path where your project is located.
3. Run the script by typing:

   `python install_dependencies.py`

### Step 3: Prepare Input Folder
Create a folder named "input" in the project directory and place the files you want sorted into this folder.
1. In the Command Prompt, create the folder by running:

   `mkdir input`

2. Manually place the files you want sorted into the "input" folder.

### Step 4: Set Up Environment Variables
This project uses environment variables which are stored in a `.env` file.
1. Locate the `.env_template` file in the project directory.
2. Create a copy of `.env_template` and rename it to `.env`.
3. Open the `.env` file in a text editor and fill in the necessary information.

### Step 5: Configure `sort_files.py`
Modify the `sort_files.py` script to suit your specific needs.
1. Open `sort_files.py` in a text editor.
2. Adjust line 21 to the relevant topic as per your requirement.

### Step 6: Run the Main Script
Finally, run the main script of the project.
1. Make sure the Command Prompt is still open and you are in the project's root directory.
2. Execute the script by running:

   `python sort_files.py`

3. Follow any on-screen instructions to complete the process.

## Support
For any queries or issues, please open an issue on the project's GitHub page or contact the maintainer at [your-email@example.com].
