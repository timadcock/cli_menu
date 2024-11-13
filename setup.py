from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Simple CLI based menu"

setup(
       # the name must match the folder name 'verysimplemodule'
        name="cli_menu",
        version=VERSION,
        author="Tim Adcock",
        author_email="timothyadcock21@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),

        classifiers= [
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux",
        ]
)