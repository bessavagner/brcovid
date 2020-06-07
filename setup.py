import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='brcovid',
    version='1.0',
    author="Vagner Bessa",
    author_email="bessavagner@gmail.com",
    description="Ler dados da covid-19 de estados ou cidades brasileiras.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bessavagner/brcovid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    'requests'
    ]
 )