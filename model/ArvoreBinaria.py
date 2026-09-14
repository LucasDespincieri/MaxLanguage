class No:
    def __init__(self, codigo, posicaoArquivo):
        self.codigo = codigo
        self.posicaoArquivo = posicaoArquivo
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo, posicaoArquivo):

        novo = No(codigo, posicaoArquivo)

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
            noPai.esquerda = novo
        else:
            noPai.direita = novo

    def buscar(self, codigo):

        noAtual = self.raiz

        while noAtual is not None:
            if codigo == noAtual.codigo:
                return noAtual

            if codigo < noAtual.codigo:
                noAtual = noAtual.esquerda
            else:
                noAtual = noAtual.direita

        return None

    def excluirNo(self, codigo):
        self.raiz = self._excluir(self.raiz, codigo)

    def _excluir(self, noAtual, codigo):
        if noAtual is None:
            return None

        if codigo < noAtual.codigo:
            noAtual.esquerda = self._excluir(noAtual.esquerda, codigo)
        elif codigo > noAtual.codigo:
            noAtual.direita = self._excluir(noAtual.direita, codigo)

        else:

            if noAtual.esquerda is None:
                return noAtual.direita
            elif noAtual.direita is None:
                return noAtual.esquerda

            else:
                noAuxiliar = self.encontrarMenorNo(noAtual.direita)
                noAtual.codigo = noAuxiliar.codigo
                noAtual.posicaoArquivo = noAuxiliar.posicaoArquivo
                noAtual.direita = self._excluir(noAtual.direita, noAuxiliar.codigo)

        return noAtual

    def encontrarMenorNo(self, no_atual):
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual
