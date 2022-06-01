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
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirement(),
    entry_points='''
        [console_scripts]
        quick=quick.main:main
    '''
    #quick= in the quick folder look for file main and in that look for function main.
    
)