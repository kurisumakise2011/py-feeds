from setuptools import find_packages, setup

setup(
    name='py-feeds',
    version='1.0',
    platforms=['POSIX'],
    packages=find_packages(),
    description='App for monitoring news feed by some keywords',
    author='Vladyslav Nahaiev',
    author_email='vlad.nagaev.vn@gmail.com',
    install_requires=['aiohttp',
                      'aiohttp_jwt',
                      'aiohttp_cors',
                      'aiohttp_security',
                      'bcrypt',
                      'mysql-connector-python',
                      'pyyaml',
                      'PyJWT']
)
