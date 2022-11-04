from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='badchttp',
    version='0.1.1',
    packages=find_packages(include=['src']),
    install_requires=["flask"],
    entry_points={
        'console_scripts': ['badchttp=src.badchars:entrypoint']
    }
)
