"""
    This script installs 'melancholia'.
"""

from distutils.core import setup
setup(name='melancholia',
      version='1.0',
      py_modules=['melancholia'],
      author='Jacek Pierzchlewski',
      author_email='jap@es.aau.dk',
      url='https://www.irfducs.org/melancholia',
      license=7'BSD 2-clause',
      platforms='Linux, OS X',
      description='Print Numpy arrays in a human readable way',
      long_description = """Module prints Numpy arrays in a human readable way. Nice looking human readable way.
      Arrays can be printed to a string variable or directly to a file."""
      )
