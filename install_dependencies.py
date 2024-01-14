import subprocess
import os 

# Set cwd to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Replace this with the path to your requirements.txt file
requirements_file = 'requirements.txt'

try:
    with open(requirements_file, 'r') as file:
        for line in file:
            package = line.strip()
            if package:
                print(f"Installing {package}...")
                subprocess.run(["pip", "install", package], check=True)

    print("All packages installed successfully.")

except FileNotFoundError:
    print(f"Could not find '{requirements_file}'. Please check the path.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while installing packages: {e}")
