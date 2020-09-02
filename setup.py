import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name= "deposito_watcher", # Replace with your own username
    # package_dir= {'':'src'},
    packages=setuptools.find_packages(),
    install_requires=["numpy>=1.16.2",
    "pymongo>=3.7.2",
    "scipy>=1.4.1",
    "pandas>=0.25.0",
    "xmltodict>=0.12.0"
    ],
    version="0.0.1",
    author="João Antônio Marcolan",
    author_email="jamarcolan@gmail.com",
    description="Pacote para fazer a gestão dos dados comportamentais para o envio para o MongoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmarcolan/etho_nosql",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)