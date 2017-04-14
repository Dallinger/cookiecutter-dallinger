# {{cookiecutter.experiment_name}}

{{cookiecutter.experiment_description}}

This is an example dallinger experiment. You can import and run it from a
python prompt or script:

    from dallinger.experiments import {{cookiecutter.experiment_name}}
    exp = {{cookiecutter.experiment_name}}()
    exp.run(mode=u'debug', vebose=True)

You can also run the experiment from the experiment directory using the
dallinger command line:

    dallinger debug
