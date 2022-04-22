from setuptools import setup, find_packages

setup(
    name='webpurify-cli',
    version='1.0.0',
    author='Raja Ravi',
    author_email='r.rajaravi@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    description="""
webpurify-cli
=============

https://www.webpurify.com/

Profanity Check for text and image along with Content Moderation

Getting it
~~~~~~~~~~

To download, either fork this github repo or simply use Pypi via pip.

.. code:: sh

   $ pip install webpurify-cli

Using it
~~~~~~~~

::

   Usage: webpurify-cli [OPTIONS] COMMAND [ARGS]...

   Options:
     --help  Show this message and exit.

   Commands:
     addwordtoblacklist       This function is used to add a word to the set
                              of...

     addwordtowhitelist       This function adds a word to an 'allowed' list...
     checkimage               This fuction submits an image to the checked for...
     checkimagestatus         This fuction should be used to poll the
                              webPurify...

     checknudityinimage       This function checks the % of nudity in an image
     checktext                This function should be used to check a string
                              or...

     removewordfromblacklist  This fuction removes a word added either through...
     removewordfromwhitelist  This function removes a word to an 'allowed'
                              list...

     replacetext              This function is used to replace profanity in
                              the...

    """,
    install_requires=[
        'Click',
        'toolz==0.11.2'
    ],
    url='https://github.com/rrajaravi/webpurify-cli.git',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
    ],
    entry_points={
        'console_scripts': [
            'webpurify-cli = webpurify_cli.webpurify:cli',
        ],
    },
)