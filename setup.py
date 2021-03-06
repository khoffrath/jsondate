import setuptools


setuptools.setup(
    name='jsondate',
    version='0.1.3',
    url='https://github.com/khoffrath/jsondate',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    description='JSON with datetime support (Python 3 compatible)',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[''],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
