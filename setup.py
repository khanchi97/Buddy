from setuptools import setup

setup(
    name="work",
    version="0.1",
    install_requires=[
        'click',
    ],
    # console script entrypont
    entry_points='''
        [console_scripts]
        work=launch:work
    ''',
)
