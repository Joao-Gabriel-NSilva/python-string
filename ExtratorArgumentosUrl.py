class ExtratorArgumentodUrl:
    def __init__(self, url):
        if self.UrlEhValida(url) and url.startswith("https://www.bytebank.com.br/"):
            self.url = url.lower()
        else:
            raise LookupError("URL inválida!!!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extraiArgumentos()
        representacao_string = "Valor: {}\nMoeda de origem: {}\nMoeda de destino: {}".format(self.extraiValor(), moedaOrigem, moedaDestino)
        return  representacao_string

    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url

    @staticmethod
    def UrlEhValida(url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):
        busca_moeda_origem = "moedaorigem=".lower()
        busca_moeda_destino= "moedadestino=".lower()


        indice_inicial_moeda_origem = self.buscaIndiceInicial(busca_moeda_origem)
        indice_final_moeda_origem   = self.url.find("&")

        moedaOrigem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indice_inicial_moeda_origem = self.buscaIndiceInicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find("&")

            moedaOrigem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.buscaIndiceInicial(busca_moeda_destino)
        indice_final_moeda_detino = self.url.find("&valor")

        moedaDestino = self.url[indice_inicial_moeda_destino:indice_final_moeda_detino]

        return moedaOrigem, moedaDestino,


    def buscaIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)

    def extraiValor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.buscaIndiceInicial(busca_valor)
        valor = self.url[indice_inicial_valor:]

        return valor
