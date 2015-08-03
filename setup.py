"""
Flask-Migrate-DB2
--------------

SQLAlchemy database migrations for Flask applications using Alembic.

Adapted to allow the use of IBM DB2.
"""
from setuptools import setup


setup(
    name='Flask-Migrate',
    version='1.5.2',
    url='http://github.com/FvD/flask-migrate/',
    license='MIT',
    author='Miguel Grinberg',
    author_email='miguelgrinberg50@gmail.com',
    description=('SQLAlchemy database migrations for Flask applications '
                 'using Alembic'),
    long_description=__doc__,
    packages=['flask_migrate'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'Flask-SQLAlchemy>=1.0',
        'alembic>=0.6',
        'Flask-Script>=0.6',
        'ibm-db>=2.0.5',
        'ibm-db-sa>=0.3.2',
        'ibm-db-alembic'
    ],
    test_suite="tests",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
