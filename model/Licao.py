from model.ArvoreBinaria import ArvoreBinaria
from model.Gerenciador import Gerenciador

class Licao:

    def __init__(self, tabelaIdioma):
        self.arvore = ArvoreBinaria()
        self.arquivo = Gerenciador("licao.txt")
        self.tabelaIdioma = tabelaIdioma
        self.carregarArvore()

    def carregarArvore(self):
        with open (self.arquivo.caminhoArquivo, 'r', encoding='utf-8') as arquivo:
            posicaoAtual = arquivo.tell()
            linha = arquivo.readline()

            while linha:
                dados = linha.strip().split(";")

                if len(dados) >= 1 and dados[0].isdigit():
                    codigo = int(dados[0])
                    self.arvore.inserir(codigo, posicaoAtual)

                posicaoAtual = arquivo.tell()
                linha = arquivo.readline()


    def adicionarLicao(self,codigo, titulo, codIdioma):
        if self.arvore.buscar(codigo) is not None:
            print(f"O codigo inserido({codigo}) já existe na tabela de lição")
            return

        idiomaPertencente = self.tabelaIdioma.buscarIdioma(codIdioma)

        if idiomaPertencente is None:
            print(f"O codigo inserido({codIdioma}) não existe na tabela de idioma")
            return

        string = f"{codigo};{titulo};{codIdioma}"
        posicao = self.arquivo.gravarRegistro(string)
        self.arvore.inserir(codigo, posicao)

        print(f"Licao de codigo {codigo} inserida com sucesso")


    def buscarLicao(self, codigo):
        noEncontrado = self.arvore.buscar(codigo)

        if noEncontrado is not None:
            linha = self.arquivo.lerRegistro(noEncontrado.posicaoArquivo)
            dados = linha.strip().split(";")

            if len(dados) == 3:
                return {
                    "codigo": int(dados[0]),
                    "titulo": dados[1],
                    "codIdioma": int(dados[2])
                }

        return None