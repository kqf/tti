from setuptools import setup, find_packages

setup(
    name="portray",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tti=portray.__main__:main",
        ],
    },
)
