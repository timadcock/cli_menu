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
        install_requires=[], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux",
        ]
)