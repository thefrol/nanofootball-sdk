from setuptools import setup, find_packages
from os.path import join, dirname

with open('requirements.txt','r') as f:
    requirements=f.readlines()

setup(
    name='nanofootball',
    version='0.1.0',
    packages=find_packages(where='src'),
    long_description='A SDK for working with nanofootball.com',
    package_dir={"": "src"},
    requires=requirements,
    entry_points={
    'console_scripts': [
        'nf = nanofoot.cli:main',
    ],
},
)