"""
Flaskcord
-------------

An Discord OAuth2 flask extension.
"""

import re
import os

from setuptools import setup, find_packages


def __get_version():
    with open("flaskcord/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)


requirements = [
    "Flask",
    "pyjwt>=2.4.0",
    "requests",
    "oauthlib",
    "cachetools",
    "requests_oauthlib",
]


on_rtd = os.getenv('READTHEDOCS') == 'True'
if on_rtd:
    requirements.append('sphinxcontrib-napoleon')
    requirements.append('Pallets-Sphinx-Themes')

extra_requirements = {
    'docs': [
        'sphinx>=7.4.6'
    ]
}


setup(
    name='Flaskcord',
    version=__get_version(),
    url='https://github.com/Vinny-Bot/Flaskcord',
    license='MIT',
    author='The Cosmos & Vinny contributors',
    author_email='dev@vinny.pp.ua',
    description='Discord OAuth2 extension for Flask.',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    extras_require=extra_requirements,
    classifiers=[
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
