from setuptools import find_packages, setup
from typing import List

# Special string used in requirements.txt to install the current project in editable mode
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.
    
    Steps:
    1. Open the file and read all lines.
    2. Strip newline characters from each line.
    3. Remove the special '-e .' entry if present (since pip install -e . 
       is handled separately when installing the project itself).
    """
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines into a list
        requirements = file_obj.readlines()
        
        # Strip newline characters from each requirement
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if it exists in the list
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# Setup function defines metadata and configuration for your package
setup(
    name='ML-Proj',  # Project name
    version='0.0.1',  # Initial version
    author='Aayushman',  # Author name
    author_email='aayushmansingh051@gmail.com',  # Author contact email
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=get_requirements('requirements.txt'),  # Dependencies from requirements.txt
)
