from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function is use to return list of requiremnets'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('/n',"") for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements









setup(
name = 'my_project', # package name
version = '0.0.1',  # Version
author = 'Vardhman ajmera', # Your name
author_email = 'vardhmanajmera76@gmail.com',
packages = find_packages(), # Automatically finds packages find_packages() detects it only if __init__.py is present.
install_requires=get_requirements('requirements.txt') 
)