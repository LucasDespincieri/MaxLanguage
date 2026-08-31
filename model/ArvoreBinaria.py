class No:
    def __init__(self, codigo, posicao_arquivo):
        self.codigo = codigo
        self.posicao_arquivo = posicao_arquivo
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo, posicao_arquivo):

        novo = No(codigo, posicao_arquivo)

        if self.raiz is None:
            self.raiz = novo
            return

        noAtual = self.raiz
        noPai = None

        while noAtual is not None:
            noPai = noAtual

            if codigo < noPai.codigo:
                noAtual = noPai.esquerda
            else:
                noAtual = noPai.direita

            if codigo < noPai.codigo:
                noPai.esquerda = noAtual
            else:
                noPai.direita = noAtual

    def buscar(self, codigo):
        pass

    def excluir(self, codigo, posicao_arquivo):
        pass
