#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages


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

setup_args = dict(
    name='{{cookiecutter.package_name}}',
    version='0.1.0',
    description='{{cookiecutter.experiment_description}}',
    long_description=readme + '\n\n' + history,
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.author_github}}/{{cookiecutter.repo_name}}',
    packages=find_packages('.'),
    package_dir={'': '.'},
    namespace_packages=['{{cookiecutter.namespace}}'],
    include_package_data=True,
    install_requires=[
        'setuptools',
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

setup(**setup_args)
