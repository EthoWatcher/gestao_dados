
#! python
"""HELLO CLI
Usage:
    ergue_sgbd.py <name>

Options:
    <name>  Arquivo que contém as junções [default: db_juncao_melhorada.json ]
"""

import deposito_watcher.cadastra_arquivos_mongo as c_a_m
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DEMO 1.0')

    if arguments['<name>']:
        path_experimento = str(arguments['<name>'])
        # path_experimento = "./modelo/db_juncao_melhorada.json"

        c_a_m.create_usuario()
        c_a_m.creat_experimento("jmarcolan")

        # Lugar aonde esta o banco de dados.
        
        c_a_m.cadastra_batch_arquivos(path_experimento, "jmarcolan", "fluoxetina_gian")