"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "autoflake==1.3.1",
    "bandit==1.6.2",
    "black==19.3b0",
    "bumpversion==0.5.3",
    "coverage==4.5.4",
    "coveralls[yaml]==1.8.2",
    "doc8==0.8.0",
    "flake8==3.7.8",
    "flake8-bandit==2.1.1",
    "flake8-broken-line==0.1.1",
    "flake8-bugbear==19.8.0",
    "flake8-builtins==1.4.1",
    # TODO when we have a better formatter "flake8-commas==2.0.0",
    "flake8-comprehensions==2.2.0",
    "flake8-debugger==3.1.0",
    "flake8-fixme==1.1.1",
    "flake8-isort==2.7.0",
    "flake8-mutable==1.2.0",
    "flake8-logging-format==0.6.0",
    "flake8-variables-names==0.0.1",
    "isort==4.3.21",
    "mccabe==0.6.1",
    "pip==19.2.2",
    "pep8-naming==0.8.2",
    "pycodestyle==2.5.0",
    "pydocstyle==4.0.1",
    "pyflakes==2.1.1",
    "pytest==5.1.0",
    "pytest-cov==2.7.1",
    "pytest-runner==5.1",
    "pyupgrade==1.22.1",
    "Sphinx==2.1.2",
    "tox==3.13.2",
    "twine==1.13.0",
    # TODO too old dependencies "wemake-python-styleguide==0.8.1",
    "wheel==0.33.5",
]

setup_requirements = ["pytest-runner==5.1"]

test_requirements = ["pytest==5.1.0"]

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
    version="2019.08.16",
    zip_safe=False,
)
