import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="covid19-es-py",
    version="1.0.0",
    description="Scraper de casos de COVID-19 no Espírito Santo",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/atilioa/covid19-es-py",
    author="Atílio Antônio",
    author_email="atiliodadalto@protonmail.com",
    license="GLP-3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["covid19-es-py"],
    include_package_data=True,
    install_requires=["beautifulsoup4", "requests"]
)
