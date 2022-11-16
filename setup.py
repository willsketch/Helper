from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
 name= 'helper',
 version= '0.0.1',
 author= 'william mwine',
 author_email= 'williammwine219@gmail.com',
 license= 'MIT License',
 description='guide you with terminal and git commands',
 long_description=long_description,
 url=''
)
