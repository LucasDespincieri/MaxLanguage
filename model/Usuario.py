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

    def adicionarUsuario(self, codigo, nome, codIdioma):
        if self.arvore.buscar(codigo) is not None:
            print(f"codigo inserido ({codigo}) já existe na tabela de usuário")
            return

        idiomaEscolhido = self.tabelaIdioma.buscarIdioma(codIdioma)

        if idiomaEscolhido is None:
            print(f"codigo inserido({codigo}) não pertence a nenhum idioma")
            return

        nivel = 1
        pontuacaoXP = 0

        string = f"{codigo};{nome};{codIdioma};{nivel};{pontuacaoXP}"
        posicao = self.arquivo.gravarRegistro(string)
        self.arvore.inserir(codigo, posicao)

        print(f"Usuario {nome} matriculado para o idioma {idiomaEscolhido['nome']} com sucesso")



    def buscarUsuario(self, codigo):
        noEncnotrado = self.arvore.buscar(codigo)

        if noEncnotrado is not None:
            linha = self.arquivo.lerRegistro(noEncnotrado.posicaoArquivo)
            dados = linha.strip()

            if len(dados) == 5:
                return {
                    "codigo": int(dados[0]),
                    "nome": dados[1],
                    "cod_idioma": int(dados[2]),
                    "nivel": int(dados[3]),
                    "pontuacao": int(dados[4])
                }
            return None

