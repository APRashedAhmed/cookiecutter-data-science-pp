import versioneer
from setuptools import setup, find_packages

setup(name='{{ cookiecutter.folder_name }}',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='{{ cookiecutter.open_source_license }}',
      author='{{ cookiecutter.author_name }}',
      packages=find_packages(),
      description='{{ cookiecutter.description }}',
      )
