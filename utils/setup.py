from importlib.metadata import entry_points
from setuptools import setup


with open('README.md') as fp:
    description = fp.read()

def load_requirements(file_name):
    '''load all the requirements from a python requirements.txt file'''
    with open(file_name) as fp:
        reqs = fp.readlines()
        return list(reqs)


setup(
    name= 'fsudb',
    description='Florida State University Intenrnal Database for CMS HGCAL Testing',
    version = '0.1.0',
    packages = ['fsudb'],
    #entry_points = {'console_scripts': ['fsudbd = fsudb.httpd:main',]},
    #install_requires = load_requirements()
    license='MIT',
    author = 'Ali Al Kadhim',
    url = 'https://github.com/AliAlkadhim/FSU_HGCAL_DB/fsudb',
    install_requires = ['numpy', 'pandas', sqlite3,
                       ]

)
