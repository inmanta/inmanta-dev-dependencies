from setuptools import setup, find_packages

setup(
    name='inmanta-dev-dependencies',
    version='2.77.0',
    description='Package collecting all common dev dependencies of inmanta modules and extensions to synchronize dependency '
                'versions.',
    author='Inmanta <code@inmanta.com>',
    license='Apache-2.0',
    packages=find_packages(),
    package_data={'inmanta_dev_dependencies': ['*']},
    python_requires='>=3.9',
    extras_require={
        'module': ['pytest-inmanta'],
        'core': ['asyncpg>=0.21.0,<1.0.0', 'pytest-env==0.8.2', 'pytest-postgresql==5.0.0', 'psycopg2==3.1.9', 'tornado==6.1'],
        'extension': ['pytest-inmanta-extensions', 'asyncpg>=0.21.0,<1.0.0', 'pytest-env==0.8.2', 'pytest-postgresql==5.0.0', 'psycopg2==3.1.9', 'tornado==6.1'],
        'async': ['pytest-asyncio==0.21.0', 'pytest-timeout==2.1.0'],
        'pytest': ['pytest-env==0.8.2', 'pytest-cover==3.0.0', 'pytest-randomly==3.12.0', 'pytest-xdist==3.3.1', 'pytest-sugar==0.9.7', 'pytest-instafail==0.5.0'],
        'sphinx': ['inmanta-sphinx==1.7.0', 'sphinx-argparse==0.4.0', 'sphinx-autodoc-annotation==1.0-1', 'sphinx-tabs', 'sphinx==6.2.1', 'sphinxcontrib-serializinghtml==1.1.5', 'sphinxcontrib-redoc==1.6.0', 'sphinx-click==4.4.0', 'recommonmark', 'myst_parser==2.0.0']
    },
    install_requires=[
        'black==23.3.0',
        'flake8==6.0.0',
        'flake8-copyright==0.2.4',
        'flake8-black==0.3.6',
        'flake8-isort==6.0.0',
        'isort==5.12.0',
        'lxml==4.9.3',
        'mypy==1.4.1',
        'pytest==7.4.0',
        'pep8-naming==0.13.3',
        'pyadr==0.19.0'
    ],
)
