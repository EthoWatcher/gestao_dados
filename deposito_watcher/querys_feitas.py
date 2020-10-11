import deposito_watcher.eto_mongo as et_m
import deposito_watcher.etho_dados as et_d
from collections import OrderedDict 
import pandas as pd 

class Transforma_Estrutura_Dados_Panda():
    def __init__(self, data_descritores):
        self.data_descritores = data_descritores
        self.keys = self._get_keys()
        self.dic_pandas = self._motor()
        self.df = self._constroi_data_frame()
    
    def get_df(self):
        return self.df

    def _constroi_data_frame(self):
        df = pd.DataFrame(self.dic_pandas, columns=self.keys)
        return df


    def _get_keys(self):
        data = self.data_descritores
        def get_keys(array):
            return array[0]

        keys =[]
        for d in data[0]:
            keys.append(list(d.keys()))

        keys = list(map(get_keys,keys))
        return keys

    def _motor(self):
        data = self.data_descritores
        keys = self.keys

        def cons_map_by_key(key):
            def map_va(data):
                return data[key]
            return map_va
        dic = {}
        for i,key in enumerate(keys):
            d= []
            for juncao in data:
                d.append(juncao[i])
                dic[keys[i]]= list(map(cons_map_by_key(keys[i]),d))
        
        return dic


class Transforma_Estrutura_Dados_Panda_list_dados(Transforma_Estrutura_Dados_Panda):
    def __init__(self, data_descritores):
        super().__init__(data_descritores)

    def _constroi_data_frame(self):
        lis_keys = list(self.dic_pandas.keys())
        t_etografias = len(self.dic_pandas[lis_keys[0]])
        l_df = []
        for i in range(t_etografias):
            dic_saida = self._filter(lis_keys,i)
            l_df.append((pd.DataFrame(dic_saida, columns=self.keys)))

        # def create_mapa(index):
        #     def maping(dic_pandas):
        #         pass
        # df = pd.DataFrame(self.dic_pandas, columns=self.keys)
        result = pd.concat(l_df)
        return result

    def _filter(self, lis_keys, index):
        # df = pd.DataFrame(self.dic_pandas, columns=self.keys)
        def constori_filter_index(index):
            def filter_vetor(numero_vetor):
                i, vetor = numero_vetor
                r_index_i = i == index
                return r_index_i
            return filter_vetor 
        
        def map_segundo_elemento(tupla):
            return tupla[1]
        dict_saida = {}
        for key in lis_keys:
            lis_saida = list(map(map_segundo_elemento, filter(constori_filter_index(index),enumerate(self.dic_pandas[key]))))
            dict_saida[key] = lis_saida[0]
        return dict_saida

        # return

# class Get_CSV():
#     def __init__(self, query):
#         self.dict_query = query
#         self.descriotres_experimento = []

#     def _get_cursor(self):
#         j = Get_Juncoes(self.dict_query)
#         cursor = j.get_cursor()
#         return cursor

#     def set_descritores_experimentais(self, li_str_descritores, li_str_categora ):
#         # isso aqui tem que melhorar uma Etografia é para lidar com o mongo e a outroa para dar um parser nos dados
#         def get_etografias(juncao):
#             eto = et_m.Etografia()
#             eto = eto.get_by_hash(juncao["id_eto"])
#             e_dados = et_d.Etografia(eto.cliente.data)
#             return {"eto": e_dados, "id_j": str(juncao["_id"])}


#         self.cursor = self._get_cursor()
#         l_u_eto_jun_id = list(map(get_etografias, self.cursor ))
#         des_experimental = Constru_descritor_experimental(li_str_descritores, li_str_categora)
#         self.descriotres_experimento = des_experimental.get_descritores_etografia(l_u_eto_jun_id)
#         return self.descriotres_experimento
#     def set_descritores_episodeo_comportamento(self):
#         pass

#     def set_variaveis_quadros(self):
#         pass

####################################################################################
# Refatorar todos esse nomes.
class Construcao_descritor_etografia():
    #  list_des_etografia =["nome", "trecho", "q_inicial", "q_final"]
    def __init__(self, list_des_etografia, query):
        self.dict_query = query
        self.lis_de_juncao = self._add_a_coluna_f(list_des_etografia)
    
    def _add_a_coluna_f(self,list_var_rastreamento):
        r_tem_ja_um_q_inicial = "q_inicial" in list_var_rastreamento
        r_tem_ja_um_q_final = "q_final" in list_var_rastreamento

        saida = []
        if not r_tem_ja_um_q_inicial:
            saida.append("q_inicial")
        if not r_tem_ja_um_q_final:
            saida.append("q_final")

        for var in list_var_rastreamento:
            saida.append(var)

        return saida



    def _get_cursor(self):
        j = Get_Juncoes(self.dict_query)
        cursor = j.get_cursor()
        return cursor
    
    def _get_lista_etografia(self):
        def get_etografias(juncao):
            eto = et_m.Etografia()
            eto = eto.get_by_hash(juncao["id_eto"])
            e_dados = et_d.Etografia(eto.cliente.data)
            return {"eto": e_dados, "id_j": str(juncao["_id"])}

        l_u_eto_jun_id = list(map(get_etografias, self._get_cursor() ))
        return l_u_eto_jun_id

    def get_descritor(self):
        list_etogra_u_junc = self._get_lista_etografia()
        descritores_pegados = []

        for eto_junca in list_etogra_u_junc:
            descritores = self._get_descritores(eto_junca["eto"])

            descritores.append(self._list_juncao_iguais(descritores, eto_junca))
            descritores_pegados.append(descritores)


        return self._ageitando_saida(descritores_pegados)

    def _ageitando_saida(self, descritores_pegados):
        self.tr = Transforma_Estrutura_Dados_Panda_list_dados(descritores_pegados)
        self.df = self.tr.get_df()
        return self.df

    def _list_juncao_iguais(self, descritores_eto, eto_junca):
        key = list(descritores_eto[0].keys())
        ls_keys = []
        for i in range(len(descritores_eto[0][key[0]])):
            ls_keys.append(eto_junca["id_j"])
        

        dic_saida = {
                "id_j": ls_keys,
                'info' : "Identificador unico da juncao"
            }
        return dic_saida
        

    # Pega todos os descritores da lista configurada
    def _get_descritores(self, etografia):
        li = []
        for descritor in self.lis_de_juncao:
            d = self._get_proces(etografia, descritor)
            li.append(d.resultado)
        
        return li

    def _get_proces(self, etografia, nome):
        if nome == "nome":
            return et_d.Descritores_nome_categoria_etografia(etografia,"")
        elif nome == "trecho":
            return et_d.Descritores_trecho_categoria_etografia(etografia,"")
        elif nome == "q_inicial":
            return et_d.Descritores_q_inicio_categoria_etografia(etografia,"")
        elif nome == "q_final":
            return et_d.Descritores_q_fim_categoria_etografia(etografia,"")
        elif nome == "q_inicio_analise":
            return et_d.Descritores_inicio_analise(etografia,"")
        elif nome == "fps":
            return et_d.Descritores_fps(etografia,"")
        else:
            pass
            # assert False
            # raise("Nao implementado o descritor")
        
    

class Constru_descritor_rastreamento():
    #  list_var_rastreamento =["@f", "@vd", "q_inicial", "q_final"]
    # o do frame sempre add
    def __init__(self, list_var_rastreamento, query):
        self.dict_query = query
        self.list_var_rastreamento = self._add_a_coluna_f(list_var_rastreamento)
    
    def _add_a_coluna_f(self,list_var_rastreamento):
        r_tem_ja_um_f = "@f" in list_var_rastreamento
        saida = []
        if r_tem_ja_um_f:
            saida = []  
        else:
            saida = ["@f"]

        for var in list_var_rastreamento:
            saida.append(var)

        return saida
    
    def _get_cursor(self):
        j = Get_Juncoes(self.dict_query)
        cursor = j.get_cursor()
        return cursor
    
    def _get_lista_rastreamento(self):
        def get_rastreamento(juncao):
            rastr = et_m.Rastreamento()
            rastr = rastr.get_by_hash(juncao["id_tra"])
            r_dados = et_d.Rastreamento(rastr.cliente.data)
            return {"rastr": r_dados, "id_j": str(juncao["_id"])}


        l_u_eto_jun_id = list(map(get_rastreamento, self._get_cursor() ))
        return l_u_eto_jun_id

    def get_descritor(self):
        list_etogra_u_junc = self._get_lista_rastreamento()

        descritores_pegados = []
        for ras_junca in list_etogra_u_junc:
            descritores = self._get_descritores(ras_junca["rastr"])

            descritores.append(self._list_juncao_iguais(descritores, ras_junca))
            descritores_pegados.append(descritores)

        # return descritores_pegados

        return self._ageitando_saida(descritores_pegados)

    def _ageitando_saida(self, descritores_pegados):
        self.tr = Transforma_Estrutura_Dados_Panda_list_dados(descritores_pegados)
        self.df = self.tr.get_df()
        return self.df


    def _list_juncao_iguais(self, descritores_ras, eto_junca):
        key = list(descritores_ras[0].keys())
        ls_keys = []
        for i in range(len(descritores_ras[0][key[0]])):
            ls_keys.append(eto_junca["id_j"])

        dic_saida = {
                "id_j": ls_keys,
                'info' : "Identificador unico da juncao"
            }
        return dic_saida
        

    
    def _get_descritores(self, rastrea):
        li = []
        for descritor in self.list_var_rastreamento:
            d = self._get_proces(rastrea, descritor)
            li.append(d.resultado)
        
        return li

    def _get_proces(self, rastreamento, nome):
        return et_d.Descritor_variavel_Rastreamento(rastreamento,nome)




class Constru_descritor_juncao():
    # lis_de_juncao = ["sexo", "dosagem", "unidade"]
    def __init__(self, lis_des_juncao, query):
        self.lis_de_juncao = lis_des_juncao
        self.dict_query = query

    def _get_cursor(self):
        j = Get_Juncoes(self.dict_query)
        cursor = j.get_cursor()
        return cursor

    def get_descritor(self):
        descritores_pegados = []
        l_juncao = self._get_cursor()

        for juncao in l_juncao:   
            descritores = self._get_descritores(juncao)

            descritores.append({
                "id_j": str(juncao["_id"]),
                'info' : "Identificador unico da juncao"
            })
            descritores_pegados.append(descritores)
        # return descritores_pegados
    
        return self._ageitando_saida(descritores_pegados)

    def _ageitando_saida(self, descritores_pegados):
        self.tr = Transforma_Estrutura_Dados_Panda(descritores_pegados)
        self.df = self.tr.get_df()
        return self.df

    def _get_proces(self, juncao, categoria):
        return et_d.Descritor_Juncao_experimento(juncao, categoria)
        

    # l uniao juncao
    def _get_descritores(self, juncao):
        li = []
        for descritor in self.lis_de_juncao:
            d = self._get_proces(juncao, descritor)
            li.append(d.resultado)
        
        return li






# menor string tem que morfa maior
class Constru_descritor_experimental():
    def __init__(self, li_str_descritores, li_str_cate, query):
        self.li_str_descritores= li_str_descritores
        self.li_str_cate = li_str_cate
        self.dict_query = query
    
    def _get_cursor(self):
        j = Get_Juncoes(self.dict_query)
        cursor = j.get_cursor()
        return cursor
    
    def _get_proces(self, nome, etografia, categoria):
        if nome == "duracao":
            return et_d.Descritor_duracao_expe_cate(etografia, categoria)
        elif nome == "duracao_total":
            # categoria aqui nao é usado para nada 
            return et_d.Descritor_duracao_experimento(etografia,categoria)
        elif nome == "frequencia":
            return et_d.Descritor_frequencia_expe_cate(etografia, categoria)
        elif nome == "latencia":
            return et_d.Descritor_latencia_expe_cate(etografia, categoria)
        elif nome == "quadro_inicial_experimento":
            return et_d.Descritor_quadro_inicio_experimento(etografia, categoria)
        elif nome == "quadro_final_experimento":
            return et_d.Descritor_quadro_fim_experimento(etografia, categoria)
        elif nome == "duracao_experimento":
            return et_d.Descritor_duracao_experimento(etografia,categoria)
        elif nome == "path_experimento":
            return et_d.Descritor_nome_caminho_experimento(etografia, categoria)

            
    
    def _get_descritores(self, etografia):
        lis_descritores= []
        for str_categoria in self.li_str_cate:
            for str_des in self.li_str_descritores:
                des = self._get_proces(str_des, etografia, str_categoria)
                lis_descritores.append(des.get_resultado())
        
        return lis_descritores

    def _get_vetor_dados(self):
        def get_etografias(juncao):
            eto = et_m.Etografia()
            eto = eto.get_by_hash(juncao["id_eto"])
            e_dados = et_d.Etografia(eto.cliente.data)
            return {"eto": e_dados, "id_j": str(juncao["_id"])}
        cursor = self._get_cursor()
        l_u_eto_jun_id = list(map(get_etografias,cursor))
        return l_u_eto_jun_id

    # terminar
    # unicao entre etografias e o id da juncao
    def get_descritores_etografia(self):
        l_u_eto_jun_id = self._get_vetor_dados()
        descritores_pegados = []
        for u_eto_jun_id in l_u_eto_jun_id:
            lis_descritores= self._get_descritores(u_eto_jun_id["eto"])

            lis_descritores.append({
                "id_eto": str(u_eto_jun_id["eto"].data["_id"]),
                'info' : "Identificador unico da etografia"
            })
            lis_descritores.append({
                "id_j": u_eto_jun_id["id_j"],
                'info' : "Identificador unico da juncao"
            })

            descritores_pegados.append(lis_descritores) 
        
        # return descritores_pegados

        return self._ageitando_saida(descritores_pegados)

    def _ageitando_saida(self, descritores_pegados):
        self.tr = Transforma_Estrutura_Dados_Panda(descritores_pegados)
        self.df = self.tr.get_df()
        return self.df
####################################################################################
            

class Get_Juncoes():
    def __init__(self, query):
        self.cli = et_m.Cliente(colecao="Juncoes")
        self.query = query
        self.cursor = self.cli.query(self.query)

    def get_cursor(self):
        return self.cursor

