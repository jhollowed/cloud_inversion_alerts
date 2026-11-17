# This is the main setup config file, which allows local installaton of the package via pip.
# From the top-level directory (location of this file), simply run `pip install .`
# For more info, see the guidelines for minimal Python package structure at
# https://python-packaging.readthedocs.io/en/latest/minimal.html

from setuptools import setup

setup(name='cloud_inversion_alerts',
      version='0.1',
      description='Tool for identifying temperature inversions with low cloud decks at select locations, and configuring email alerts',
      url='https://github.com/jhollowed/cloud_inversion_alerts',
      author='Joe Hollowed',
      author_email='hollowed@umich.edu',
      packages=['cloud_inversion_alerts'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
