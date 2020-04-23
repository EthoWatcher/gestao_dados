class Descritor:
    pass

# calcula em segundos a duração do experimento
class Descritor_duracao_expe_cate():
    def __init__(self, etografia, categoria):
        self.eto = etografia
        self.cat = categoria
        self.resultado = {f'd_e_{self.cat}_s':self._calcula(), "info":f'Duração do comportamento {self.cat} no experimento (s)'}


    def _calcula(self):
        dura = 0
        for anota in self.eto.get_anotacoes_eto_categoria(self.cat):
            dura = dura + anota["@frameFinal"] - anota["@frameInicial"]
        
        dura = dura /self.eto.dados_videos["fps"]
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



class Etografia:
    def __init__(self, data):
        self.data = data
        self.anotacoes = self.data["analiseEtografica"]["dadosAnalise"]["analises"]["analise"]
        self._add_nome_categoria_anotacao()
        self._get_dados_video()


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