from importlib.metadata import entry_points
from setuptools import setup, find_packages

def read_requirement():
    #function to read requirements from a file
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

setup(
    name='quick',
    version='0.1.5',
    packages=find_packages(),
    include_package_data=True,
    # install_requires=read_requirement(),
    install_requires=['click==8.1.3'],
    entry_points='''
        [console_scripts]
        quick=quick.main:main
    '''
    #quick= in the quick folder look for file main and in that look for function main.
    
)