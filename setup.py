# setup.py

from setuptools import setup, find_packages

setup(
    name="coco_mailer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Patrick Chidera",
    description="A simple package that interactswith the COCO api.",
    url="https://github.com/lordace-coder/python_coco_mailer.git",  # Optional
)
