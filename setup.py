#!/usr/bin/env python
import codecs
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


readme_rst = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='django-select2-forms',
    version='2.0.2',
    description='Django form fields using the Select2 jQuery plugin',
    long_description=codecs.open(readme_rst, encoding='utf-8').read(),
    author='Frankie Dintino',
    author_email='fdintino@theatlantic.com',
    url='https://github.com/theatlantic/django-select2-forms',
    packages=find_packages(),
    license='BSD',
    platforms='any',
    install_requires=[
        'django-sortedm2m',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    zip_safe=False)
