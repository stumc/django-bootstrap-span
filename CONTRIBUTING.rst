
How to get set up for development.
==================================

    Start with python 2.7.6
    Get pip:        see web for instructions here: http://www.pip-installer.org/en/latest/installing.html
    Get tox :       pip install tox
    Get pytest:     pip install pytest
    Get coverage :  pip install coverage
    Get pylint :    pip install pylint
    Get sphinx :    pip install sphinx
    
    The github project (from your new dev directory): 
       git clone https://github.com/stumc/django-bootstrap-span.git

How to run the tests.
=====================

Multi Python platform running before pushing:
    tox
    (I couldn't get pypy to work in my local win32 dev env, but it does in Travis CI environment)

Code coverage report:
    coverage run -m pytest
    coverage html
    # read htmlcov/index.html in your browser
    
Build the docs (also a test of the docs)
    ( cd docs ; make html ) - on Unix
    ( cd docs && make html ) - on Windows

What to include in a bug report.
================================

    1. Version of django-bootstrap-span
    2) Version of django-bootstrap
    3) Version of django
    4) Version of python
    5) Symptoms of problem (stack trace, output of html)
    6) Sample code re-creating the problem (1 file)

Coding standards, test coverage standards, documentation...
===========================================================

    tox tests passing on python 2.7, 3.4 and pypy
    pylint - shows no failures or warnings - required
    code coverage 100% - required
    Travis CI - fully passing - required
    
 Git commands reminder sheet
 ===========================
    git status
    git clone https://github.com/stumc/django-bootstrap-span.git
    # make your changes
    git log --oneline
    git add myNewFile.py
    git commit -m "Changed something"
    git remote -v
    git remote add origin https://github.com/stumc/django-bootstrap-span
    git pull origin master
    git tag -a v0.0.1 -m "the next release"
    git push origin v0.0.1
    git status
    
 Git, Documentation And Continuous Integration Links
 ===================================================
    https://github.com/stumc/django-bootstrap-span
    https://readthedocs.org/projects/django-bootstrap-span/
    https://travis-ci.org/stumc/django-bootstrap-span