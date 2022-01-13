# Dados

Essa biblioteca serve para fazer a gestão dos dados etograficos extraídos do EthoWathcer OS.

# Análise to TNF

OS dados foram análisados pelo Gian.


# Resultados

Por enquanto, foi essa biblioteca que gerou o banco de dados "C:\dados_gian_mongo_arrumados" e são elas que o notebooks apontam.

# Expansões

Essa biblioteca precisa de algumas expansões para ser usada dentro de um sistema.


# Comandos para fazer um novo pacote

```
python3 setup.py sdist bdist_wheel
```
https://packaging.python.org/tutorials/packaging-projects/


Outra forma de instalar é na pasta que esta o arquivo setup.py a linha :
```
pip install -e . 
```

O "-e" significa que vai ser dimanico para que fique atualizando



### terceira opção
```py
setup(
    extras_require={
        "dev" = ["bibliotecas para o desenvolvimento"]
    }
)
```


```
pip instal -e .["dev"]
```

## Arquivo __main__.py

O arquivo __main__.py serve para rodar com python -m nome_modulo


## Ageitando as pasta de testes
conftest.py

```
# conftest.py
@pytest.fixture(scope="module")
def funcao_que_sera_executa_antes():
    """ instancia do flask""
    return create_app()
```

# pytest-flask
```
# test_arquivo.py

def test_exemplo(app):
    print(app)


def test_exemplo(client):
    print(app)


```

# Para que fique instalando a biblioteca

Com o comando a baixo ele instala o pacote mas é necessario ter um setup.py. Todas vez que alterar os arquivos ele re-intala
```
python -m pip install -e .
```