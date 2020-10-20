
#! python
"""Linha de comando para organizar os dados no MongoDB a partir de arquivos do ethowatcher gravados no computador
Usage:
    ergue_sgbd.py <path_list_juncao_experimento> <path_descrivao_experimento>

Options:
    <path_list_juncao_experimento>  Arquivo que contém as listas de junções [default: db_juncao_melhorada.json ]
    <path_descrivao_experimento> Arquivo que contém a descrição dos experimentos
"""

import deposito_watcher.cadastra_arquivos_mongo as c_a_m
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DEMO 1.0')

    if (arguments['<path_list_juncao_experimento>'] and arguments['<path_descrivao_experimento>']):
        path_list_juncao_experimento = str(arguments['<path_list_juncao_experimento>'])
        path_descrivao_experimento  = str(arguments['<path_descrivao_experimento>'])
        # path_experimento = "./modelo/db_juncao_melhorada.json"

        c_a_m.create_usuario()
        c_a_m.creat_experimento("jmarcolan", path_descrivao_experimento)

        # Lugar aonde esta o banco de dados.
        
        c_a_m.cadastra_batch_arquivos(path_list_juncao_experimento, "jmarcolan", "fluoxetina_gian")