"""
Usage:

    pip install .

    to locally install the package via pip.
"""

import setuptools

with open("README.MD", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='super32-pkg',
    version='0.1.0',
    description='Super32 assembler parser and utilities',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/xsjad0/Super32',
    author='xsjad0',
    author_email='xsjad0@example.com',
    packages=setuptools.find_packages(),
    install_requires=[
        'bitstring',
        'python-dotenv'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
