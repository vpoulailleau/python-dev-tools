"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "bumpversion==0.5.3",
    "coverage==4.5.2",
    "coveralls[yaml]==1.6.0",
    "mccabe==0.6.1",
    "pip==19.0.2",
    "pycodestyle==2.5.0",
    "pyflakes==2.1.0",
    "pytest==4.3.0",
    "pytest-cov==2.6.1",
    "pytest-runner==4.4",
    "Sphinx==1.8.1",
    "tox==3.5.2",
    "twine==1.13.0",
    "wheel==0.33.1",
]

setup_requirements = ["pytest-runner==4.4"]

test_requirements = ["pytest==4.3.0"]

setup(
    author="Vincent Poulailleau",
    author_email="vpoulailleau@gmail.com",
    entry_points={
        "console_scripts": ["whatalinter = python_dev_tools.whatalinter:main"]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Needed and up-to-date tools to develop in Python",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="python_dev_tools",
    name="python_dev_tools",
    packages=find_packages(include=["python_dev_tools"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/vpoulailleau/python_dev_tools",
    version="2019.02.26",
    zip_safe=False,
)
