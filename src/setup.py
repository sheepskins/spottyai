from setuptools import setup, find_packages

setup(
    name='spottyai_api',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'rospy'
    ],
)