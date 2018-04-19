try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Game about a submarine',
    'author': 'Satinder Kaur',
    'url': 'https://github.com/sandykaur2008/python-game',
    'download_url': 'https://github.com/sandykaur2008/python-game',
    'author_email': 'sandykaur2008@protonmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['Game'],
    'scripts': [],
    'name': 'Game'
}

setup(**config)
