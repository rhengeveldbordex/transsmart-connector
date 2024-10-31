from setuptools import setup, find_packages

setup(
    name="transsmart_connector",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        'requests >= 2.31.0',
        'python-dotenv >= 1.0.1'
    ],
    author="Robert Hengeveld",
    author_email="rhengeveld@bordex.nl",
    description="TranssmartConnector is a Python package for connecting to the Transsmart API.",
    long_description="Transsmart Connector is a Python package to connect to the Transsmart API. It provides a simple interface to interact with the Transsmart API. The package is built on top of the requests library. The package is designed to be used in a business environment to automate the process of creating shipments, labels, and documents.",
    url="https://github.com/rhengeveldbordex/transsmart-connector",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
