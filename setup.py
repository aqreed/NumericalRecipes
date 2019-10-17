from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='numericalrecipes',
    description='Numerical Recipes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='aqreed',
    version='0.0.1',
    url='https://github.com/aqreed/NumericalRecipes',
    package_dir={'': 'src'},
    install_requires=['numpy', 'matplotlib'],
    tests_requires=['pytest']
)
