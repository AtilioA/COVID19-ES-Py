from os import path
from setuptools import find_packages, setup

thisDirectory = path.abspath(path.dirname(__file__))
with open(path.join(thisDirectory, "README.md"), encoding="utf-8") as f:
    README = f.read()

setup(
    name="COVID19-ES-Py",
    version="3.1.0",
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
        "Programming Language :: Python :: 3.8",
    ],
    keywords="covid covid19 corona coronavirus brazil espirito-santo es api",
    packages=find_packages(exclude=["*.tests/", "*.tests.*/", "tests.*/", "tests"]),
    include_package_data=True,
    install_requires=[
        "arrow==0.15.5",
        "atomicwrites==1.3.0; sys_platform == 'win32'",
        "attrs==19.3.0",
        "beautifulsoup4==4.9.0",
        "certifi==2020.4.5.1",
        "chardet==3.0.4",
        "colorama==0.4.3; sys_platform == 'win32'",
        "coverage==5.1",
        "idna==2.9",
        "importlib-metadata==1.6.0; python_version < '3.8'",
        "more-itertools==8.2.0",
        "packaging==20.3",
        "pluggy==0.13.1",
        "py==1.10.0",
        "pyparsing==3.0.0a1",
        "pytest==5.4.1",
        "pytest-cov==2.8.1",
        "python-dateutil==2.8.1",
        "requests==2.23.0",
        "six==1.14.0",
        "soupsieve==2.0",
        "urllib3==1.25.9",
        "wcwidth==0.1.9",
        "wrapt==1.12.1",
        "zipp==3.1.0",
        "rows"
    ],
)
