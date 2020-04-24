import eto_mongo as et_m
import etho_dados as et_d
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
        df = pd.DataFrame(self.dic_pandas)
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





class Get_CSV():
    def __init__(self, query):
        self.dict_query = query
        self.descriotres_experimento = []

    def _get_cursor(self):
        j = Get_Juncoes(self.dict_query)
        cursor = j.get_cursor()
        return cursor

    def set_descritores_experimentais(self, li_str_descritores, li_str_categora ):
        def get_etografias(juncao):
            eto = et_m.Etografia()
            eto = eto.get_by_hash(juncao["id_eto"])
            e_dados = et_d.Etografia(eto.cliente.data)
            return {"eto": e_dados, "id_j": str(juncao["_id"])}


        self.cursor = self._get_cursor()
        l_u_eto_jun_id = list(map(get_etografias, self.cursor ))
        des_experimental = Constru_descritor_experimental(li_str_descritores, li_str_categora)
        self.descriotres_experimento = des_experimental.get_descritores_etografia(l_u_eto_jun_id)
        return self.descriotres_experimento
    def set_descritores_episodeo_comportamento(self):
        pass

    def set_variaveis_quadros(self):
        pass





class Constru_descritor_juncao():
    # lis_de_juncao = ["sexo", "dosagem", "unidade"]
    def __init__(self, lis_des_juncao):
        self.lis_de_juncao = lis_des_juncao

    def get_descritor(self, l_juncao):
        descritores_pegados = []
        for juncao in l_juncao:   
            descritores = self._get_descritores(juncao)

            descritores.append({
                "id_j": str(juncao["_id"]),
                'info' : "Identificador unico da juncao"
            })
            descritores_pegados.append(descritores)
        return descritores_pegados

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
    def __init__(self, li_str_descritores, li_str_cate):
        self.li_str_descritores= li_str_descritores
        self.li_str_cate = li_str_cate
    
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

    
    def _get_descritores(self, etografia):
        lis_descritores= []
        for str_categoria in self.li_str_cate:
            for str_des in self.li_str_descritores:
                des = self._get_proces(str_des, etografia, str_categoria)
                lis_descritores.append(des.get_resultado())
        
        return lis_descritores

    # terminar
    # unicao entre etografias e o id da juncao
    def get_descritores_etografia(self, l_u_eto_jun_id):
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
        
        return descritores_pegados


            

class Get_Juncoes():
    def __init__(self, query):
        self.cli = et_m.Cliente(colecao="Juncoes")
        self.query = query
        self.cursor = self.cli.query(self.query)

    def get_cursor(self):
        return self.cursor



class Calcula_descritores():
    pass