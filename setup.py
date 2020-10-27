import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name= "deposito_watcher", # Replace with your own username
    # package_dir= {'':'src'},
    packages=setuptools.find_packages(exclude=("tests*","dados*", "notebooks*")), # colocar o exclude aqui exclude=["/tests","/notebooks"] exclude=['tests']
    install_requires=[
        "xmltodict",
        "pymongo",
        "numpy",
        "scipy",
        "pandas"],
    scripts=['scripts/ergue_sgbd.py'],
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
    include_package_data=True,
    package_data={"deposito_watcher": ["modelo/1-usuarios.json", # https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
                    "modelo/2-banco_experimental.json",
                    "modelo/3-juncoes.json"]
    
    }
    # data_files =  [("modelo/1-usuarios.json",
    #                 "modelo/2-banco_experimental.json",
    #                 "modelo/3-juncoes.json"])

)