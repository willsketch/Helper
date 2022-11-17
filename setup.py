from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
 name= 'helper',
 version= '0.0.3',
 author= 'william mwine',
 author_email= 'williammwine219@gmail.com',
 license= 'MIT License',
 description='guide you with terminal and git commands',
 long_description=long_description,
 url='https://github.com/willsketch/Helper',
 py_modules=['helper', 'my_helper'],
 packages= find_packages(),
 install_requires = [requirements],
 classifiers=[
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8.12',
    ],
 include_package_data=True,
 package_data={'helper':['examples.txt']},
 entry_points= {
     'console_scripts':[
         'helper = my_helper:cli',
     ]
 }
)
