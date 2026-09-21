from model.ArvoreBinaria import ArvoreBinaria
from model.Gerenciador import Gerenciador


class Usuario:

    def __init__(self, tabelaIdioma):
        self.arvore = ArvoreBinaria()
        self.arquivo = Gerenciador("usuario.txt")
        self.tabelaIdioma = tabelaIdioma
        self.carregarArvore()


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
            print(f"codigo inserido({codIdioma}) não pertence a nenhum idioma")
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
            dados = linha.strip().split(";")

            if len(dados) == 5:
                return {
                    "codigo": int(dados[0]),
                    "nome": dados[1],
                    "cod_idioma": int(dados[2]),
                    "nivel": int(dados[3]),
                    "pontuacao": int(dados[4])
                }
            return None

    def deletarUsuario(self, codigo):

        noEncontrado = self.arvore.buscar(codigo)

        if noEncontrado is None:
            print(f"Código informardo ({codigo}) não existe")
            return

        self.arquivo.excluirRegistro(noEncontrado.posicaoArquivo)
        self.arvore.excluirNo(codigo)

        print("Idioma deletado com sucesso!")

    def atualizarStatus(self, codigo, novoNivel, novaPontuacao):
        noEncontrado = self.arvore.buscar(codigo)
        usuarioAntigo = self.buscarUsuario(codigo)

        if noEncontrado is not None and usuarioAntigo is not None:
            self.arquivo.excluirRegistro(noEncontrado.posicaoArquivo)

            string = f"{codigo};{usuarioAntigo['nome']};{usuarioAntigo['cod_idioma']};{novoNivel};{novaPontuacao}"
            novaPosicao = self.arquivo.gravarRegistro(string)

            noEncontrado.posicaoArquivo = novaPosicao

    def listarTodosUsuarios(self):
        lista_usuarios = []

        def percorrerArvore(noAtual):
            if noAtual is not None:
                percorrerArvore(noAtual.esquerda)

                usuario = self.buscarUsuario(noAtual.codigo)
                if usuario is not None:
                    lista_usuarios.append(usuario)

                percorrerArvore(noAtual.direita)

        percorrerArvore(self.arvore.raiz)
        return lista_usuarios