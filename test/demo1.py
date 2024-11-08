import os

script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the project root (one level up from the script)
project_path = os.path.abspath(os.path.join(script_directory, '..'))
print(project_path)
