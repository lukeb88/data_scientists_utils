from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='data_scientists_utils',
    url='https://github.com/lukeb88/data_scientists_utils.git',
    author='Luca Brunelli',
    author_email='luca.brunelli@statwolf.com',
    # Needed to actually package something
    packages=['dataframe', 'plots', 'results'],
    # Needed for dependencies
    install_requires=reqs,
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Tools utils for data scientists',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)