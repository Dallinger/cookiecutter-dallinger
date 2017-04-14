#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
    history = pypandoc.convert('CHANGELOG.md', 'rst')
except (IOError, ImportError):
    readme = open('README.md').read()
    history = open('CHANGELOG.md').read()

# Get rid of Sphinx markup
history = history.replace('.. :changelog:', '')

doclink = """
Documentation
-------------

The full documentation is at http://{{cookiecutter.package_name}}.rtfd.org."""

setup_args = dict(
    name='{{cookiecutter.package_name}}',
    version='0.1.0',
    description='{{cookiecutter.experiment_description}}',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.author_github}}/{{cookiecutter.repo_name}}',
    packages=[
        '{{cookiecutter.package_name}}',
    ],
    package_dir={'{{cookiecutter.package_name}}': '{{cookiecutter.package_name}}'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='Dallinger {{cookiecutter.experiment_name}}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'dallinger.experiments': [
            '{{cookiecutter.experiment_class}} = {{cookiecutter.package_name}}.experiment:{{cookiecutter.experiment_class}}',
        ],
    },
)

# Read in requirements.txt for dependencies.
setup_args['install_requires'] = install_requires = []
setup_args['dependency_links'] = dependency_links = []
with open('requirements.txt') as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        if req.startswith('-e '):
            dependency_links.append(req[3:])
        else:
            install_requires.append(req)

setup(**setup_args)
