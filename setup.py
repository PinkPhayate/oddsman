from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='oddsman',
    version='0.0.2',
    author='PinkPhayate',
    author_email='pinqphayate@gmail.com',
    url='https://github.com/PinkPhayate',
    description='this module extracts odds(rate) from hourse race in japan',
    long_description=long_description,
    zip_safe=False,
    include_package_data=False,
    packages=find_packages(),
    install_requires=['bs4>=0.0.1', 'request>=0.0.13'],
    tests_require=[],
    setup_requires=[],
)
