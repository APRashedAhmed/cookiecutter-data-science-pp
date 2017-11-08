import versioneer
from setuptools import setup, find_packages

setup(name='cookiecutter-data-science-apra',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='MIT',
      author='apra93',
      packages=find_packages(),
      description='Modified data science cookiecutter',
      )
