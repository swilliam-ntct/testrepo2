from setuptools import setup

NAME = 'api-client'
PACKAGE_NAME = 'apiclient'
VERSION = '<version#>'

def readme():
    with open('README.rst') as f:
        return f.read()


#if os.environ.get('CI_COMMIT_TAG'):
#    version = os.environ['CI_COMMIT_TAG']
#else:
#    version = os.environ['CI_JOB_ID']


setup(name=NAME,
      version=VERSION,
      description='API Client',
      long_description=readme(),
      classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
      ],
      keywords='',
      url='',
      author='Steve William, NETSCOUT Systems, Inc.',
      author_email='swilliam@netscout.com',
      license='MIT',
      packages=[PACKAGE_NAME],
      install_requires=[
          'requests',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
