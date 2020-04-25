import pandas as pd 
import querys_feitas as qf


class Fusao_variaveis():
    def __init__(self, query):
        self.dict_query = query
        self.df_rastreamento = None
        self.df_etografia = None
        self.df_juncao = None
        self.df_descritores_eto = None


    def set_variaveis_rastreamento(self, list_var_rastreamento):
        # list_var_rastreamento =["@Vd", "@Van"]
        de_ras = qf.Constru_descritor_rastreamento(list_var_rastreamento, self.dict_query )
        self.df_rastreamento = de_ras.get_descritor()

    def set_variaveis_etografia(self, list_des_etografia):
        # list_des_etografia =["nome", "trecho", "q_inicial", "q_final"]
        de_eto = qf.Construcao_descritor_etografia(list_des_etografia, self.dict_query )
        self.df_etografia = de_eto.get_descritor()
        

    def set_variaveis_juncao(self, lis_de_juncao):
        # lis_de_juncao = ["sexo", "dosagem", "unidade"]
        cdj = qf.Constru_descritor_juncao(lis_de_juncao, self.dict_query )
        self.df_juncao = cdj.get_descritor() #list(cursor)

    def set_variaveis_descritore_eto_experimento(self, li_str_descritores, li_str_categora ):
        # li_str_descritores = ["duracao", "frequencia"]
        # li_str_categora = ["Immobility", "Swimming"]
        des_experimental = qf.Constru_descritor_experimental(li_str_descritores, li_str_categora, self.dict_query)
        self.df_descritores_eto = des_experimental.get_descritores_etografia()
