
How to get set up for development.
==================================

    Start with python 2.7.6
    Get pip: see web for instructions here: http://www.pip-installer.org/en/latest/installing.html
    Get tox : pip install tox
    Get pytest: pip install pytest
    Get coverage : pip install coverage
    Get pylint : pip install pylint
    The github project: http://github.com/stumc/django-bootstrap-span.git

How to run the tests.
=====================

Multi Python platform running:
    tox
    (I couldn't get pypy to work)

Code coverage report:
    coverage run -m pytest
    coverage html
    # read htmlcov/index.html

What to include in a bug report.
================================

    1. Version of django-bootstrap-span
    1b) Version of django-bootstrap
    1c) Version of django
    2. Version of python
    3. Symptoms of problem (stack trace, output of html)
    4. Sample code re-creating the problem (1 file)

Coding standards, test coverage standards, documentation...
===========================================================

    tox tests passing on 2.7 and 3.4
    pylint no failures
    code coverage 100% or more
    
 Documentation
 =============
    https://readthedocs.org/projects/django-bootstrap-span/