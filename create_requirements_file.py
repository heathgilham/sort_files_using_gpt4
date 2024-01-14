import os
import re
from importlib.metadata import version, PackageNotFoundError

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Initialize a set to hold all unique imports
libs = set()

# Walk through all files in the start_directory
for root, dirs, files in os.walk(script_directory):
    for file in files:
        if file.endswith('.py'):
            with open(os.path.join(root, file), 'r') as f:
                for line in f:
                    match = re.compile(r'^(import|from) ([a-zA-Z0-9_.]+)').match(line)
                    if match:
                        libs.add(match.group(2).split(".")[0])

# Specify the full path for the requirements.txt file
requirements_file_path = os.path.join(script_directory, 'requirements.txt')

# Write the imports to the requirements.txt file
with open(requirements_file_path, 'w') as req_file:
    for lib in sorted(libs):
        try:
            v = version(lib)
            req_file.write(f"{lib}=={v}\n")
        except PackageNotFoundError:
            continue
        
print("Requirements file created successfully.")
