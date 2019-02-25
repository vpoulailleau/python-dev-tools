#!/bin/bash

source venv/bin/activate

git rebase
git status 

echo -n "Do you want to add something in HISTORY.rst? (y/n) [n]: "
read BOOL
if [ "$BOOL" == "y" ]
then
    exit 1
fi
echo ""

echo "Running test"
python setup.py develop
make test
echo -n "Is it OK? (y/n) [y]: "
read BOOL
if [ "$BOOL" == "n" ]
then
    exit 1
fi
echo ""

echo "Delivering"
make bump
make release
git push
git push --tags
echo "Edit the release on GitHub (https://github.com/vpoulailleau/python-dev-tools/releases)"
echo "Done"

