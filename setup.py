from setuptools import setup, find_packages
import subprocess

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lic = f.read()

with open('requirements.txt') as f:
    required = f.read()

setup(
    name='town_transport',
    version='0.0.1',
    description='Send publi email package',
    long_description=readme,
    author='Manuel Castillo-Lopez',
    author_email='manucalop@gmail.com',
    url='https://github.com/manucalop/python_project_template',
    license=lic,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=required
)

subprocess.run("rm -rf build", shell=True, check=True)
subprocess.run("rm -rf *.egg-info", shell=True, check=True)
subprocess.run("rm -rf dist", shell=True, check=True)
