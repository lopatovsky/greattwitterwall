from setuptools import setup

with open('README') as f:
    long_description = ''.join(f.readlines())

setup(
    name='greattwitterwall',
    version='0.3',
    description='Search for the tweets and display them as the web app.',
    long_description=long_description,
    keywords='twitter,search,web',
    author='Lukas Lopatovsky',
    author_email='lopatovsky@gmail.com',
    license='Public Domain',
    url='https://github.com/lopatovsky/greattwitterwall',
    py_modules=['greattwitterwall'],
    classifiers=[
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        ],
)
