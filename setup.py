'''
Created on 27 Jan 2017

@author: annub
'''
from setuptools import setup

setup(name='systeminfo', 
      description='Basic system Information for COMP3067',
      url='',
      author='annub',
      author_email='anurakta.behera@ucdconnect.ie',
      license= 'GPL3',
      packages=['systeminfo'],
      entry_points={
          'console_scipts':['comp3067_systeminfo=systeminfo.main:main']
          }
      )