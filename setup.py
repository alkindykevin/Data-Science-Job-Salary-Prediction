from setuptools import find_packages, setup  # Importing necessary functions from setuptools
from typing import List  # Importing List type from typing module

HYPEN_E_DOT = '-e .'  # Defining a constant for a specific string pattern

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads requirements from a file and returns them as a list.
    '''
    requirements = []  # Initializing an empty list to store requirements
    with open(file_path) as file_obj:  # Opening the requirements file
        requirements = file_obj.readlines()  # Reading lines from the file
        requirements = [req.replace("\n", "") for req in requirements]  # Removing newline characters from each requirement
        if HYPEN_E_DOT in requirements:  # Checking if a specific pattern exists in the requirements list
            requirements.remove(HYPEN_E_DOT)  # Removing the pattern from the requirements list
    return requirements  # Returning the list of requirements extracted from the file

# Setting up the project with necessary details
setup(
    name='Data Science Salary Prediction',  # Name of the project
    version='0.0.1',  # Version number of the project
    author='Kevin Alkindy',  # Name of the author
    author_email='alkindy.ka@gmail.com',  # Email address of the author
    packages=find_packages(),  # Finding all packages within the project
    install_requires=get_requirements('requirements.txt')  # Installing required dependencies from a file
)
