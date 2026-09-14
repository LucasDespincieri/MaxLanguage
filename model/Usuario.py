from model.ArvoreBinaria import ArvoreBinaria
from model.Gerenciador import Gerenciador


class Usuario:

    def __init__(self, tabelaIdioma):
        self.arvore = ArvoreBinaria()
        self.arquivo = Gerenciador("usuario.txt")
        self.tabelaIdioma = tabelaIdioma


    def carregarArvore(self):
        with open (self.arquivo.caminhoArquivo, 'r', encoding='utf-8') as arquivo:
            posicaoAtual = arquivo.tell()
            linha = arquivo.readline()

            while linha:
                dados = linha.strip().split(';')

                if len(dados) >= 1 and dados[0].isdigit():
                    codigo = int(dados[0])
                    self.arvore.inserir(codigo, posicaoAtual)

                posicaoAtual = arquivo.tell()
                linha = arquivo.readline()