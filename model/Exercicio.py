from model.ArvoreBinaria import ArvoreBinaria
from model.Gerenciador import Gerenciador


class Exercicio:

    def __init__(self, tabelaLicao, tabelaIdioma):
        self.arvore = ArvoreBinaria()
        self.arquivo = Gerenciador("exercicio.txt")
        self.tabelaIdioma = tabelaIdioma
        self.tabelaLicao = tabelaLicao
        self.carregarArvore()


    def carregarArvore(self):
        with open(self.arquivo.caminhoArquivo, 'r', encoding='utf-8') as arquivo:
            posicaoAtual = arquivo.tell()
            linha = arquivo.readline()

            while linha:
                dados = linha.strip().split(";")

                if len(dados) >= 1 and dados[0].isdigit():

                    codigo = int(dados[0])
                    self.arvore.inserir(codigo, posicaoAtual)

                posicaoAtual = arquivo.tell()
                linha = arquivo.readline()


    def adicionarExercicio(self, codigo, codLicao, nivelDificuldade,
                           tipo, descricao, opcoes, resposta, pontuacao):

        if self.arvore.buscar(codigo) is not None:
            print(f"O codigo inserido({codigo}) já existe na tabela de exercício")
            return

        licaoPertencente = self.tabelaLicao.buscarLicao(codLicao)

        if licaoPertencente is None:
            print(f"O codigo de licao inserido({codLicao}) não existe na tabela de Lição")
            return

        codIdioma = licaoPertencente['codIdioma']
        idiomaEncontrado = self.tabelaIdioma.buscarIdioma(codIdioma)
        nomeIdioma = idiomaEncontrado['nome'] if idiomaEncontrado else "Desconhecido"

        string = (f"{codigo};{codLicao};{nivelDificuldade};{tipo};{descricao};{opcoes};"
                  f"{resposta};{pontuacao}")

        posicao = self.arquivo.gravarRegistro(string)
        self.arvore.inserir(codigo, posicao)

        print(f"Exercício adicionado à lição '{licaoPertencente['titulo']}' do idioma {nomeIdioma}")

    def buscarExercicio(self, codigo):
        noEncontrado = self.arvore.buscar(codigo)

        if noEncontrado is not None:
            linha = self.arquivo.lerRegistro(noEncontrado.posicaoArquivo)
            dados = linha.strip().split(';')

            if len(dados) == 8:
                lista_opcoes = dados[5].split('|')

                return {
                    "codigo": int(dados[0]),
                    "codLicao": int(dados[1]),
                    "nivelDificuldade": int(dados[2]),
                    "tipo": int(dados[3]),
                    "descricao": dados[4],
                    "opcoes": lista_opcoes,
                    "respostaCorreta": dados[6],
                    "pontuacao": int(dados[7])
                }
        return None
