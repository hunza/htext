from setuptools import setup, find_packages
import sys, os

version = '0.4.0'

setup(name='htext',
      version=version,
      description="htext.ja - helpers for handling japanese text",
      long_description="""\
htext.ja is helper library for handling japanese text.
""",
      classifiers=filter(None, map(str.strip, """\
Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License
Programming Language :: Python
""".splitlines())),
      keywords='',
      author='Chihio SAKATOKU',
      author_email='csakatoku@gmail.com',
      url='https://github.com/hunza/htext',
      license='MIT License',
      platforms=['any'],
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      test_suite='nose.collector'
      )
