from setuptools import setup, find_packages

setup(
    name="llmk",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'ipykernel>=6.0',
        'jupyter-client>=7.0'
    ],
    entry_points={}
)
