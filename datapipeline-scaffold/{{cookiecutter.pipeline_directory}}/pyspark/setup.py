from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='pyspark jobs for {{ cookiecutter.pipeline_directory }}',
    author='{{ cookiecutter.pipeline_owner }}',
)
