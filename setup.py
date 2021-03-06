from setuptools import setup, find_packages

setup(
    name='EDSA',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    url='https://github.com/DanielJHarty/EDSA',
    author='Daniel Harty',
    author_email='danieljohnharty2@gmail.com'
)