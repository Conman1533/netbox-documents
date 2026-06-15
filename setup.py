from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

with open(path.join(top_level_directory, 'requirements.txt')) as file:
    required = [
        line.strip() for line in file.read().splitlines()
        if line.strip() and not line.strip().startswith('#')
    ]

setup(
    name='newdoc',
    version='0.0.1',
    description='Attach documents and external URLs to any NetBox object',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jason Yates',
    author_email='me@jasonyates.co.uk',
    url='https://github.com/jasonyates/netbox-documents',
    install_requires=required,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords=['netbox', 'netbox-plugin', 'plugin'],
)
