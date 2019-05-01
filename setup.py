from setuptools import setup, find_packages


setup(
    name='numericalrecipes',
    description='Numerical Recipes',
    author='aqreed',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    test_suite='test'
)
