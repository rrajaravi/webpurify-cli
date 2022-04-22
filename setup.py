from setuptools import setup, find_packages

setup(
    name='webpurify-cli',
    version='0.1.0',
    author='Raja Ravi',
    author_email='r.rajaravi@gmail.com',
    packages=find_packages(),
    include_package_data=True,
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