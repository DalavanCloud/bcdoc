#!/usr/bin/env python
import sys


from setuptools import setup


requires = ['six>=1.8.0,<2.0.0',
            'docutils>=0.10']


if sys.version_info[:2] == (2, 6):
    # For python2.6 we have a few other dependencies.
    # First we need an ordered dictionary so we use the
    # 2.6 backport.
    requires.append('ordereddict==1.1')


setup(
    name='bcdoc',
    version='0.14.0',
    description='ReST document generation tools for botocore.',
    long_description=open('README.rst').read(),
    author='Amazon Web Services',
    url='https://github.com/botocore/bcdoc',
    packages=['bcdoc'],
    package_dir={'bcdoc': 'bcdoc'},
    install_requires=requires,
    license='Apache License 2.0',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
