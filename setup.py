from setuptools import setup

setup(
    name="buddy",
    version="0.1",
    py_modules = ['launch','chain','util'],
    install_requires=[
        'click',
    ],
    # console script entrypont
    entry_points='''
        [console_scripts]
        buddy=launch:work
    ''',
)
