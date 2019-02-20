# Dallinger Cookiecutter

This repository contains a template for creating a simple Dallinger experiment
using [cookiecutter](https://cookiecutter.readthedocs.io). To use this
template, you'll first need to install `cookiecutter` using `pip`:

    pip install cookiecutter


Then you can create a new experiment package in the current directory using
the following command:

    cookiecutter https://github.com/Dallinger/cookiecutter-dallinger.git

This will provide you with prompts for the following information about your
experiment:

- `repo_name`: The GitHub repository name where experiment package will 
eventually live. This should not contain any spaces or special characters
other than `-` and `_`.

- `package_name`: The python package name for your experiment. This should
be all lower case and not contain any spaces or special characters other
than `_`.

- `experiment_name`: A name for your experiment.

- `experiment_class`: The python class name for your custom experiment
class. This should not contain any spaces or special characters.

- `experiment_description`: A short description of your experiment

- `author`: The package author's full name

- `author_email`: The contact email for the experiment author.

- `author_github`: The GitHub account name where the package will
eventually live.


Once you've answered those questions a new directory named with the
`repo_name` you provided will be created. The package in that directory will
contain a basic Dallinger experiment, an example Bot that runs through the
experiment as a simulated browser, an automated test harness, and
documentation generation tools. The package can be installed with pip (`pip
install -e .`) and/or uploaded to the [Python Package Index
(PyPI)](https://pypi.python.org/pypi).

To being developing the package you will need to install the development
requirements, using the command:

    pip install -r dev-requirements.txt

Then you can run the test suite and validation tools using the `tox` command.

Your experiment package will also contain a `Vagrantfile` which is intended to
create and configure virtual machines using [Vagrant](https://www.vagrantup.com/).
Once you've installed Vagrant, you should be able to use `vagrant up` from the
experiment directory to create a Linux virtual machine with dallinger and its
dependencies installed, and `vagrant ssh` to connect to it. More details can
be found in the [Dallinger documentation](https://dallinger.readthedocs.io/en/latest/vagrant_setup.html)
