from os import path
from setuptools import find_packages, setup

# read the contents of your README file
thisDirectory = path.abspath(path.dirname(__file__))
with open(path.join(thisDirectory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="COVID19-ES-Py",
    version="1.0.3",
    description="Scraper de boletins de casos de COVID-19 no Espírito Santo.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/atilioa/COVID19-ES-Py",
    author="Atílio Antônio",
    author_email="atiliodadalto@protonmail.com",
    license="GLP-3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["beautifulsoup4", "requests"]
)
