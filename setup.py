# setup.py
from setuptools import setup, find_packages

setup(
    name='django_advanced_password_validators',
    version='0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.0',
    ],
    description='A Django package for custom password validation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shanathvemula/django_advanced_password_validators',
    author='Shanath Kumar Vemula',
    author_email='shanath1213@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
