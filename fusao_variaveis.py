import pandas as pd 
import querys_feitas as qf


class Fusao_variaveis():
    def __init__(self, query):
        self.dict_query = query
        self.df_rastreamento = pd.DataFrame()
        self.df_etografia = pd.DataFrame()
        self.df_juncao = pd.DataFrame()
        self.df_descritores_eto = pd.DataFrame()
        self.df_fundido = pd.DataFrame()
        self.l_dfs = []


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
        # nome
        # li_str_descritores = ["duracao", "frequencia"]
        # li_str_categora = ["Immobility", "Swimming"]
        des_experimental = qf.Constru_descritor_experimental(li_str_descritores, li_str_categora, self.dict_query)
        self.df_descritores_eto = des_experimental.get_descritores_etografia()

    def _fusao_by_id_j(self, df1, df2):
        return pd.merge(df1, df2, on='id_j')


    def get_dados_fundidos(self):
        df_saida = self._calcula_regras()
        return df_saida
        # regras = self._calcula_regras()
        # if regras["r_existe_var_juncao"]:
        #     pass

    def _fund_eto_rast(self):
        def filtra_pedaco(id_j, df):
            saida =  df[df['id_j']==id_j]
            return saida

        
        valores_unicos = set(self.df_etografia["id_j"])
        self._arruma_df_eto()

        df_merged = []
        for id_j in valores_unicos:
            df_eto = filtra_pedaco(id_j, self.df_etografia)
            df_rat = filtra_pedaco(id_j, self.df_rastreamento)
            df_rat = df_rat.drop(['id_j'], axis=1)
            df_merge_col = pd.merge(df_eto, df_rat, on='@f')
            df_merged.append(df_merge_col)
        
        result = pd.concat(df_merged)
        return result



    def _arruma_df_eto(self):        
        def linha_to_df(l):
            mult = l["q_fim"]-l["q_inicio"]
            if mult == 0 or mult ==-1:
                return pd.DataFrame()
            else:
                q = l["q_fim"]   - l["q_inicio"]

                l["@f"] = l["q_inicio"]

                # keys = list(l.keys())
                # multiplica todos os valores para ter a quantidade certa
                for key in l.keys():
                    ls =[]
                    for i in range(q):
                        ls.append(l[key])
                    l[key] = ls

                # mappa a coluna do #@f
                for i, valor in enumerate(l["@f"]):
                    l["@f"][i] = valor + i 

                # converte to um dic
                dic_saida = {}
                for key in l.keys():
                    dic_saida[key] = l[key]

                d = pd.DataFrame(dic_saida)
                return d
        saida = []

        for index, row in self.df_etografia.iterrows():
            df = linha_to_df(row)
            r_df_existe = df.empty
            if not r_df_existe:
                saida.append(df)
        self.df_etografia = pd.concat(saida)


    def _calcula_regras(self):
        d_mesclar = []
        r_existe_var_juncao = not self.df_juncao.empty
        r_existe_var_des_exp = not self.df_descritores_eto.empty
        r_existe_var_eto = not self.df_etografia.empty
        r_existe_var_ras = not self.df_rastreamento.empty
        
        # if r_existe_var_juncao:
        #     self.l_dfs.append({"df": self.df_juncao, "fus": ["id_j"]})
        # if r_existe_var_des_exp:
        #     self.l_dfs.append({"df": self.df_descritores_eto, "fus": ["id_j"]})
        # if r_existe_var_eto:
        #     self.l_dfs.append({"df": self.df_etografia, "fus": ["id_j","@f"]})
        # if r_existe_var_ras:
        #     self.l_dfs.append({"df": self.df_descritores_eto, "fus": ["id_j","@f"]})
        # isso daqui tem que ser melhorado mas me diverti escrevendo assim
        # amanha refatorar esse pedaco
        if r_existe_var_juncao:
            d_mesclar.append(self.df_juncao)
        if r_existe_var_des_exp:
            d_mesclar.append(self.df_descritores_eto)
        if r_existe_var_ras and r_existe_var_eto:
            d_mesclar.append(self._fund_eto_rast())
        elif r_existe_var_ras:
            d_mesclar.append(self.df_rastreamento)
        elif r_existe_var_eto:
            d_mesclar.append(self.df_etografia)
        
        return self._mesclando(d_mesclar)

    def _mesclando(self, d_mesclar):
        r_tem_df = len(d_mesclar) >0

        if r_tem_df:
            df_saida = d_mesclar.pop()
            for df_merge in d_mesclar:
                df_saida = self._fusao_by_id_j(df_saida, df_merge)

            return df_saida

        else:
            return pd.DataFrame()
            