from setuptools import setup, find_packages

VERSION = '1.1.3'
DESCRIPTION = 'Python CLI for accessing protein .fasta sequences using the UNIPROT API.'
LONG_DESCRIPTION = 'This package contains a CLI that returns a proteins fasta sequence to the shell.'

# Setting up
setup(
        name="get-uniprot",
        version=VERSION,
        author="James Sanders",
        author_email="james.sanders1711@gmail.com",
        url = 'https://github.com/J-E-J-S/get-uniprot',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'requests==2.20.0',
            'click==7.1.2'
        ],
        entry_points = {
            'console_scripts':['uniprot=getUniprot.uniprot:cli']
        }
)
