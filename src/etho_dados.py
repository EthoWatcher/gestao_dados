class Descritor:
    def __init__(self, etografia, categoria):
        self.eto = etografia
        self.cat = categoria
        self.resultado = None

    def get_resultado(self):
        return self.resultado

# fusao descritor experimental com etografia ou 

# fusao etografia com rastreamento



class Descritores_nome_categoria_etografia(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'categoria':self._calcula(), "info":f'Nome da categoria marcada'}

    def _calcula(self):
        def map_nome(anotaca):
            return anotaca["@nome"]
        dura =  list(map(map_nome, self.eto.anotacoes ))
        
        return dura

class Descritores_trecho_categoria_etografia(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'trecho':self._calcula(), "info":f'Sequencia de anotacao'}
    def _calcula(self):
        def map_nome(anotaca):
            return anotaca["@ponto"]
        dura =  list(map(map_nome, self.eto.anotacoes ))
        
        return dura

class Descritores_q_inicio_categoria_etografia(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'q_inicio':self._calcula(), "info":f'Quadro inicial do comportamento'}
    def _calcula(self):
        def map_nome(anotaca):
            return anotaca["@frameInicial"]
        dura =  list(map(map_nome, self.eto.anotacoes ))
        
        return dura

class Descritores_q_fim_categoria_etografia(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'q_fim':self._calcula(), "info":f'Quadro final do comportamento'}
    def _calcula(self):
        def map_nome(anotaca):
            return anotaca["@frameFinal"]

        dura =  list(map(map_nome, self.eto.anotacoes ))
        return dura

# class Descritores_categorias_experimento(Descritor):
#     def __init__(self, etografia, categoria):
#         super().__init__(etografia, categoria)
#         self.resultado = {f'anotacoes':self._calcula(), "info":f'Quadro inicial do experimento'}

#     def _calcula(self):
#         dura =  self.eto.anotacoes
#         return dura


## Refatorar esse documento para melhor posicionar


class Descritor_quadro_inicio_experimento(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'q_inicio_experimento':self._calcula(), "info":f'Quadro final do experimento'}

    def _calcula(self):
        dura =  self.eto.dados_videos["frameProces"]
        return dura

class Descritor_quadro_fim_experimento(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'q_final_experimento':self._calcula(), "info":f'Quadro inicial do experimento'}

    def _calcula(self):
        dura =  self.eto.dados_videos["frameFinal"]
        return dura



class Descritor_duracao_experimento(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'd_total_experimento':self._calcula(), "info":f'Duração do experimento (s)'}

    def _calcula(self):
        dura =  self.eto.dados_videos["frameFinal"] - self.eto.dados_videos["frameProces"]
        dura = dura/self.eto.dados_videos["fps"]
        return dura


class Descritor_nome_caminho_experimento(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'path_experimento':self._calcula(), "info":f'Nome da categoria marcada'}

    def _calcula(self):
        path_etografia = self.eto.dados_videos["nomeVxml"]
        return path_etografia



class Descritor_Juncao_experimento(Descritor):
    def __init__(self, junca_data, categoria):
        super().__init__(junca_data, categoria)
        self.resultado = {f'{categoria}':self._calcula(), "info":f'variavel independente'}

    def _calcula(self):
        r_tem_no_dic = self.cat in self.eto["var_ind"]
        if r_tem_no_dic:
            return self.eto["var_ind"][self.cat]
        else:
            return ""


        

# class Descritor_trecho(Descritor):
#     def __init__(self, etografia, categoria):
#         super().__init__(etografia, categoria)
#         self.resultado = {f'trecho_e_{self.cat}_s':self._calcula(), "info":f'Duração do comportamento {self.cat} no experimento (s)'}

#     def _calcula(self):
#         return 


# calcula em segundos a duração do experimento
class Descritor_duracao_expe_cate():
    def __init__(self, etografia, categoria):
        self.eto = etografia
        self.cat = categoria
        self.resultado = {f'd_e_{self.cat}_s':self._calcula(), "info":f'Duração do comportamento {self.cat} no experimento (s)'}

    def _ajuste(self):
        return 0
        # seq = self.eto.get_anotacoes_eto_categoria(self.cat)
        # ultimo_elemento= self.eto.anotacoes[len(self.eto.anotacoes)-1]
        # r_ultima_categoria = ultimo_elemento["@nome"] == self.cat
        # ajuste = 0
        # if r_ultima_categoria:
        #     ajuste = len(seq) -1
        # else:
        #     ajuste = len(seq)

        # return ajuste / self.eto.dados_videos["fps"] 

    def _calcula(self):
        dura = 0
        for anota in self.eto.get_anotacoes_eto_categoria(self.cat):
            dura = dura + anota["@frameFinal"] - anota["@frameInicial"]
        
        dura = dura /self.eto.dados_videos["fps"]
        dura = dura + self._ajuste()
        return dura
 

    def get_resultado(self):
        return self.resultado


class Descritor_latencia_expe_cate():
    def __init__(self, etografia, categoria):
        self.eto = etografia
        self.cat = categoria
        self.resultado = {f'l_e_{self.cat}_s':self._calcula(), "info":f'Latencia do comportamento {self.cat} no experimento (s)'}


    def _calcula(self):
        ano = self.eto.get_anotacoes_eto_categoria(self.cat)
        r_categoria_anotada = len(ano) >0
        late = 0
        if r_categoria_anotada:
            late = ano[0]["@frameInicial"] - self.eto.dados_videos["frameProces"]
        else:
            late = self.eto.dados_videos["frameFinal"]

        late = late /self.eto.dados_videos["fps"]
        return late
 

    def get_resultado(self):
        return self.resultado



class Descritor_frequencia_expe_cate():
    def __init__(self, etografia, categoria):
        self.eto = etografia
        self.cat = categoria
        self.resultado = {f'f_e_{self.cat}_s':self._calcula(), "info":f'Frequencia do comportamento {self.cat} no experimento'}


    def _calcula(self):
        freq = len(self.eto.get_anotacoes_eto_categoria(self.cat)) 
        return freq
 

    def get_resultado(self):
        return self.resultado


class Descritor_variavel_Rastreamento(Descritor):
    def __init__(self, etografia, categoria):
        super().__init__(etografia, categoria)
        self.resultado = {f'{categoria}':self._calcula(), "info":f'Rastreamento'}
        # self.categoria = categoria

    def _calcula(self):
        def map_nome(anotaca):
            return anotaca[f'{self.cat}']

        variavel =  list(map(map_nome, self.eto.anotacao_ras ))
        
        return variavel




class Rastreamento:
    def __init__(self, data):
        self.data = data
        self.anotacao_ras = self.data["analiseProcessaImage"]["dadosAnalise"]["anaProceImagem"]["area"]["proce"]
        self.escala = float(self.data["analiseProcessaImage"]["dadosVideoAnalisado"]["escala"])
        self.fps = float(self.data["analiseProcessaImage"]["dadosVideoAnalisado"]["fps"])
        self.parser_rastreamento()
        self._arrumando_escala()

    def _arrumando_escala(self):
        
        for anotacao in self.anotacao_ras:
            # a escala ficar em cm por s
            anotacao["@Vd"] = anotacao["@Vd"]  * 1/self.escala * self.fps
            # convertendo para cm (tem que conferir)
            anotacao["@Valt"] = anotacao["@Valt"]  * 1/self.escala
            anotacao["@Vlar"] = anotacao["@Vlar"]  * 1/self.escala

            # convertendo para cm}{{2
            anotacao["@Var"] = anotacao["@Var"]  * 1/self.escala * 1/self.escala

            

    def parser_rastreamento(self):
        for anotacao in self.anotacao_ras:
            anotacao["@f"] = int(anotacao["@f"])
            anotacao["@arP"] = float(anotacao["@arP"])
            anotacao["@arM"] = float(anotacao["@arM"])
            anotacao["@ceX"] = float(anotacao["@ceX"])
            anotacao["@ceY"] = float(anotacao["@ceY"])
            anotacao["@altP"] = float(anotacao["@altP"])
            anotacao["@altM"] = float(anotacao["@altM"])
            anotacao["@larP"] = float(anotacao["@larP"])
            anotacao["@larM"] = float(anotacao["@larM"])
            anotacao["@an"] = float(anotacao["@an"])


            anotacao["@Var"] = float(anotacao["@Valt"])
            anotacao["@Vd"] = float(anotacao["@Valt"])
            anotacao["@Valt"] = float(anotacao["@Valt"])
            anotacao["@Vlar"] = float(anotacao["@Valt"])
            anotacao["@Van"] = float(anotacao["@Valt"])





class Etografia:
    def __init__(self, data):
        self.data = data
        self.anotacoes = self.data["analiseEtografica"]["dadosAnalise"]["analises"]["analise"]
        self._add_nome_categoria_anotacao()
        self._arbritrariedade_lidar_ambiguidade()
        self._get_dados_video()

    def _arbritrariedade_lidar_ambiguidade(self):
        pass
        # tamanho = len(self.anotacoes) - 1
        # for i, anotacao in enumerate(self.anotacoes):
        #     r_ultima_anotacao = i >= tamanho
        #     if r_ultima_anotacao:
        #         anotacao["@frameFinal"] = anotacao["@frameFinal"] 
        #     else:
        #         anotacao["@frameFinal"] = anotacao["@frameFinal"] - 1



    def get_dados_video_analisado(self):
        return self.dados_videos


    def get_anotacoes_eto_categoria(self, categoria):
        def fil_ano(anota):
            r_anotaca = categoria == anota["@nome"]
            return r_anotaca
        
        anotacao = list(filter(fil_ano, self.anotacoes))
        return anotacao


    def _get_dados_video(self):
        self.dados_videos = self.data["analiseEtografica"]["dadosVideoAnalisado"]
        self.dados_videos["fps"] = float(self.dados_videos["fps"])
        self.dados_videos["frameProces"] = int(self.dados_videos["frameProces"])
        self.dados_videos["frameFinal"] = int(self.dados_videos["frameFinal"])
        # self.q_inicial = self.data["analiseEtografica"]["dadosVideoAnalisado"]["frameProces"]
        # self.q_final   = self.data["analiseEtografica"]["dadosVideoAnalisado"]["frameFinal"]
        # self.fps = self.data["analiseEtografica"]["dadosVideoAnalisado"]["frameFinal"]
    

    def _get_categoria_by_id(self, id_b):
        nome_cate = ""
        for categoria in self.data["analiseEtografica"]["dadosCatalago"]["Categorias"]["categoria"]:
            r_encontro_categoria = id_b == categoria["@id"]
            if r_encontro_categoria:
                nome_cate = categoria["@nome"]
                break

        return nome_cate


    def _add_nome_categoria_anotacao(self):
        # def con_int(valor):
        for anotacao in self.data["analiseEtografica"]["dadosAnalise"]["analises"]["analise"]:
            anotacao["@nome"] = self._get_categoria_by_id(anotacao["@id"])
            anotacao["@frameFinal"] = int(anotacao["@frameFinal"])
            anotacao["@frameInicial"] = int(anotacao["@frameInicial"])
            anotacao["@ponto"] = int(anotacao["@ponto"])