#!/bin/bash -x

python3 setup.py sdist
twine upload dist/* --verbose
