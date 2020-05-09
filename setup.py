import sys
from setuptools import setup

long_description = None
if sys.version_info[0] < 3:
    with open('README.md') as f:
        long_description = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name="chord_manager_cli",
    version="0.2",

    author="Kevin Chang",
    author_email="kevin.chaohwa.chang@gmail.com",

    description="command line tools for simplifying music chords",
    long_description=long_description,

    packages=["chord_manager_cli"],
    install_requires=[
        "pychord",
        "click"
    ],

    entry_points={
        "console_scripts": [
            "cm = chord_manager_cli.cli:main"
        ]
    },
)