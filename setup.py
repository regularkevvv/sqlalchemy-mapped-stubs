from setuptools import setup, find_packages

setup(
    name="sqlalchemy-mapped-stubs",
    version="2.0.31.1",
    packages=find_packages(),
    package_data={"sqlalchemy-stubs": ["**/*.pyi"]},
    install_requires=["sqlalchemy==2.0.31"],  # Adjust the version as needed
    zip_safe=False,
    description="Stubs for SQLAlchemy 2.0' Mapped types",
    long_description="Type stubs for the MApped types in SQLAlchemy 2.0",
    author="Kev",
    author_email="hola@kev.pe",
    url="https://github.com/regularkevvv/sqlalchemy-mapped-stubs",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Stubs Only",
    ],
)
