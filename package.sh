#!/bin/bash -x

rm -rf dist
python3 setup.py sdist
twine upload dist/* --verbose
