from setuptools import setup, find_packages

setup(
    name="inmanta-dev-dependencies",
    version="2.77.0",
    description="Package collecting all common dev dependencies of inmanta modules and extensions to synchronize dependency versions.",
    author="Inmanta",
    author_email="support@inmanta.com",
    packages=find_packages(),
    python_requires=">=3.9,<4.0",
    include_package_data=True,
    install_requires=[
        "requests",
        "pydantic",
        "jsonschema",
        "PyYAML",
        "tinydb",
        "netaddr",
        "prettytable",
        "click-log",
        "Jinja2",
        "fuzzywuzzy",
        "python-Levenshtein",
        "more-itertools",
        "typing-extensions",
        "chardet"
    ],
    # entry_points={
    #     'console_scripts': [
    #         'synctool = synctool.sync.main:synctool',
    #     ],
    # },
)
