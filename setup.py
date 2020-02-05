"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "autoflake==1.3.1",
    "bandit==1.6.2",
    "black==19.10b0",
    "bumpversion==0.5.3",
    "coverage==5.0.3",
    "coveralls[yaml]==1.10.0",
    "doc8==0.8.0",
    "flake8==3.7.9",
    "flake8-2020==1.5.0",
    "flake8-bandit==2.1.2",
    "flake8-broken-line==0.1.1",
    "flake8-bugbear==20.1.4",
    "flake8-builtins==1.4.2",
    # TODO when we have a better formatter "flake8-commas==2.0.0",
    "flake8-comprehensions==3.2.2",
    "flake8-debugger==3.2.1",
    "flake8-fixme==1.1.1",
    "flake8-isort==2.8.0",
    "flake8-mutable==1.2.0",
    "flake8-logging-format==0.6.0",
    "flake8-variables-names==0.0.3",
    "isort==4.3.21",
    "mccabe==0.6.1",
    "pip==20.0.2",
    "pep8-naming==0.9.1",
    "pycodestyle==2.5.0",
    "pydocstyle==5.0.2",
    "pyflakes==2.1.1",
    "pytest==5.3.5",
    "pytest-cov==2.8.1",
    "pytest-runner==5.2",
    "pyupgrade==1.26.2",
    "Sphinx==2.3.1",
    "tox==3.14.3",
    "twine==3.1.1",
    # TODO too old dependencies "wemake-python-styleguide==0.8.1",
    "wheel==0.34.2",
]

setup_requirements = ["pytest-runner==5.2"]

test_requirements = ["pytest==5.3.5"]

setup(
    author="Vincent Poulailleau",
    author_email="vpoulailleau@gmail.com",
    entry_points={
        "console_scripts": [
            "whatalinter = python_dev_tools.whatalinter:main",
            "whataformatter = python_dev_tools.whataformatter:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Needed and up-to-date tools to develop in Python",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="python_dev_tools",
    name="python_dev_tools",
    packages=find_packages(include=["python_dev_tools*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/vpoulailleau/python-dev-tools",
    version="2020.02.05",
    zip_safe=False,
)
