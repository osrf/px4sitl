#!/usr/bin/env python3

from setuptools import setup

install_requires = [
    'rocker',
]

kwargs = {
    'name': 'px4sitl',
    'version': '0.0.1',
    'packages': ['px4sitl'],
    'package_dir': {'': 'src'},
    # 'package_data': {'rocker': ['templates/*.em']},
    'entry_points': {
        'console_scripts': [
            'iris_px4sitl = px4sitl.cli:iris',
            'plane_px4sitl = px4sitl.cli:plane',
	    ],
	},
    'author': 'Tully Foote',
    'author_email': 'tfoote@osrfoundation.org',
    'keywords': ['PX4','Gazebo', 'SITL'],
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License'
    ],
    'data_files': [
        ('share/applications', [
            'data/org.osrfoundation.iris_sitl.desktop',
            'data/org.osrfoundation.plane_sitl.desktop']),
    ],
    'description': 'Entrypoints to launch SITL based operator training',
    'long_description': 'Entrypoints to launch SITL based operator training',
    'license': 'Apache License 2.0',
    'python_requires': '>=3.0',

    'install_requires': install_requires,
    'url': 'https://github.com/tfoote/px4sitl',
    'zip_safe': False,
}

setup(**kwargs)

