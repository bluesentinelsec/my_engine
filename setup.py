from setuptools import setup, find_packages

setup(
    name='my_engine',
    version='0.1.4',
    license='GPLv3',
    author="Michael Long",
    author_email='bluesentinel@protonmail.com',
    packages=["my_engine"],
    url='https://github.com/bluesentinelsec/my_engine',
    keywords='game engine',
    install_requires=[
          'pygame',
      ],

)