import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
PACKAGES = [
    'airports',
    'airports.flightstats',
    'airports.migrations',
    'airports.openflights',
    'airports.management',
]
    
setup(
    name='django-airports-apis',
    version='0.0.2',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    license='MIT License',
    description='Airport and data for Django. Using different API Endpoints',
    long_description=README,
    url='https://github.com/illing2005/django-airports-apis',
    author='Sebastian Illing',
    author_email='s.illing@gmx.de',
    install_requires=[],    
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
