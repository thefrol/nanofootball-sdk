from setuptools import setup, find_packages
from os.path import join, dirname
from pathlib import Path

with open('requirements.txt','r') as f:
    requirements=f.readlines()

this_directory=Path(__file__).parent
long_description=(this_directory / 'README.MD').read_text(encoding='utf8')
print(long_description)


setup(
    name='nanofootball-sdk',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=requirements, # лол без этой строчки он ругался на README.MD
    entry_points={
        'console_scripts': [
            'nf = nanofoot.cli:main',
        ]
    },
    url='https://github.com/thefrol/nanofootball-sdk',
    long_description=long_description,
    long_description_content_type='text/markdown; variant=GFM',
    license="MIT"
)