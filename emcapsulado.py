class BaseDados:
    def __init__(self):
        self.__dados = {}


    def inserirDado(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_dado(self):
        for id, nome in self.__dados['clientes'].items():
            print(id,nome)

    def apaga_dado(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()
bd.inserirDado(1, 'clieto')
bd.inserirDado(2, 'chave')
bd.lista_dado()