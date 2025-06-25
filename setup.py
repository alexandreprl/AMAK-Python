from setuptools import find_packages, setup
from setuptools.command.install import install

setup(
    name='amak',
    packages=find_packages(include=['amak']),
    version='0.6.3',
    description='Simplified AMAK for Python',
    author='Alexandre Perles',
    install_requires=["pygame", "pygame_widgets"],
)