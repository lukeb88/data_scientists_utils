from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='data_scientists_utils',
    url='https://github.com/lukeb88/data_scientists_utils.git',
    author='Luca Brunelli',
    author_email='luca.brunelli@statwolf.com',
    # Needed to actually package something
    packages=['dataframe', 'plots', 'results'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas', 'sklearn', 'matplotlib'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Tools utils for data scientists',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)