from setuptools import setup, find_packages

with open('README') as f:
    long_description = ''.join(f.readlines())

setup(
    name='greattwitterwall',
    version='0.3.2',
    description='Search for the tweets and display them as the web app.',
    long_description=long_description,
    keywords='twitter,search,web',
    author='Lukas Lopatovsky',
    author_email='lopatovsky@gmail.com',
    license='Public Domain',
    url='https://github.com/lopatovsky/greattwitterwall',
    packages=find_packages(),
    zip_safe=False,    
    entry_points={
        'console_scripts': [
            'greattwitterwall = greattwitterwall.greattwitterwall:main',
        ],
    },
    install_requires=['Flask', 'click>=6', 'itsdangerous>=0.24' , 'Jinja2>=2.8',
                      'MarkupSafe>=0.23', 'requests>=2.11.1' ],
    classifiers=[
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        ],
    package_data={
        'greattwitterwall': ['templates/*.html'],
    }
)
