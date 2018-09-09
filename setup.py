from setuptools import setup

import re

with open("hubble/__main__.py", "r") as hubble_main:
    hubble_text = hubble_main.read()

version, = re.search("__version__ = \"(\d.\d.\d)\"", hubble_text).groups()

packages = ["hubble"]

with open("requirements.txt", "r") as requirements_file:
    requirements = [requirement.rstrip("\n") for requirement in requirements_file.readlines()] # noqa

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="hubble_github",
    version=version,
    description="The command-line search tool for GitHub.",
    long_description=readme,
    author="Joseph Banks",
    author_email="joseph@josephbanks.me",
    url="https://github.com/jos-b/hubble",
    packages=packages,
    package_data={"": ["LICENSE"]},
    package_dir={"hubble": "hubble"},
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=requirements,
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ]
)
