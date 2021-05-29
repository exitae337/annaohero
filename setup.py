from io import open
from setuptools import setup

version = '0.0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    
    name= 'annaohero',
    version = version,
    author = 'AnnaOhero',
    author_email='exitae337@gmail.com',
    url='https://github.com/exitae337/annaohero',
    description=(
        u'Python module for writing scripts for for building multiple files into one file and vice versa '
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['annaohero', 'tests', 'tests.files', 'tests.uncompress'],
    
)
