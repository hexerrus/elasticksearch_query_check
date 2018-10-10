from distutils.core import setup

setup(
    name='elasticksearch_query_check',
    scripts=['elasticksearch_query_check/elasticksearch_query_check'] ,
    version='0.1dev',
    packages=['elasticksearch_query_check',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
        install_requires=[
          'requests>=2.19.1',
      ],
)