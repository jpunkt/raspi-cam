import re
import ast

from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('cam/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))
    setup(
        name='raspi-cam',
        version=version,
        description='raspberry pi point-and-shoot camera',
        url='https://github.com/jpunkt/raspi-cam.git',
        author='jpunkt',
        author_email='johannes@arg-art.org',
        platforms='any',

        packages=[
            'cam'
        ],

        install_requires=[
            gpiozero,
            picamera
        ],

        entry_points='''
            
        '''

    )

