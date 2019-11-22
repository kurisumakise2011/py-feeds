from setuptools import setup

dependencies = [
    'aiohttp>=3.0.0',
    'cchardet',
    'aiodns',
    'pyjwt',
    'bcrypt',
    'aiohttp_jwt',
    'yaml',
    'aiohttp-cors',
    'aiohttp_security',
    'mysql'
]

setup(
    name='py-feeds',
    version='1.0',
    description='App for monitoring news feed by some keywords',
    author='Vladyslav Nahaiev',
    author_email='vlad.nagaev.vn@gmail.com',
    packages=['app'],
    install_requires=dependencies
)
