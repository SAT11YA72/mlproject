from setuptools import setup, find_packages
from typing import List

h = '-e .'

# def get_requirements(file_path:str)->List[str]:
#     with open(file_path, 'r') as file:
#         if h in file.read():
#             return []
#         return file.read().splitlines()

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name='mlproject_pack',
    version='0.1',
    author= 'Satya',
    author_email= 'gsp883337@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)


        