from unicodedata import digit

from model.ArvoreBinaria import ArvoreBinaria
from model.Gerenciador import Gerenciador


class Exercicio:

    def __init__(self, tabelaIdioma, tabelLicao):
        self.arvore = ArvoreBinaria()
        self.arquivo = Gerenciador("exercicio.txt")
        self.tabelaIdioma = tabelaIdioma
        self.tabelaLicao = tabelLicao
        self.carregarArvore()


    def carregarArvore(self):
        with open(self.arquivo.caminhoArquivo, 'r', encoding='utf-8') as arquivo:
            posicaoAtual = arquivo.tell()
            linha = arquivo.readline()

            while linha:
                dados = linha.strip().strip(";")

                if len(dados) >= 1 and dados[0].isdigit():

                    codigo = int(dados[0])
                    self.arvore.inserir(codigo, posicaoAtual)

                posicaoAtual = arquivo.tell()
                linha = arquivo.readline()


    def adicionarExercicio(self, codigo, codLicao, nivelDificuldade,
                           tipo, descricao, opcoes, resposta, pontucao):
        pass