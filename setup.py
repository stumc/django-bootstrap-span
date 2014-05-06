"Setup file for django-bootstrap-span"

from setuptools import setup

with open('README.rst') as fh:
    long_description = fh.read()

setup(
      name='django-bootstrap-span',
      version='0.0.1',
      description='Django bootstrap span adds class=spanN support in forms input elements',
      long_description=long_description,
      author='Stuart McMillan',
      author_email='smcmillan@usefulautomation.com',
      url='https://github.com/stumc/django-bootstrap-span',
      packages=['bootstrap_span','bootstrap_span.templatetags'],
      install_requires=['six','django','django-bootstrap'],
      classifiers=[
#        "Development Status :: 5 - Production/Stable",
        'Development Status :: 3 - Alpha',
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
      ],
)

