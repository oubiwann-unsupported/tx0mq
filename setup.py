from setuptools import find_packages, setup
import sys

setup(
    name=meta.display_name,
    version=meta.version,
    description=meta.description,
    author=meta.author,
    author_email=meta.author_email,
    url=meta.url,
    license=meta.license,
    long_description=meta.long_description,
    packages=find_packages('.'),
    long_description=open('README.rst').read(),
    install_requires=meta.requires,
)
