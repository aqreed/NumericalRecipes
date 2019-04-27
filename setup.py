from setuptools import setup, find_packages


setup(
    name='nr',
    description='Numerical Recipes',
    author='Andres Quezada Reed',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
