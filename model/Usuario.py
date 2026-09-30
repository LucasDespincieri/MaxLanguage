from model.ArvoreBinaria import ArvoreBinaria
from model.Gerenciador import Gerenciador


class Usuario:

    def __init__(self, tabelaIdioma):
        self.arvore = ArvoreBinaria()
        self.arquivo = Gerenciador("usuario.txt")
        self.tabelaIdioma = tabelaIdioma
        self.carregarArvore()

    def carregarArvore(self):
        with open(self.arquivo.caminhoArquivo, 'r', encoding='utf-8') as arquivo:
            posicaoAtual = arquivo.tell()
            linha = arquivo.readline()

            while linha:
                dados = linha.strip().split(';')

                if len(dados) >= 1 and dados[0].isdigit():
                    codigo = int(dados[0])
                    self.arvore.inserir(codigo, posicaoAtual)

                posicaoAtual = arquivo.tell()
                linha = arquivo.readline()

    def adicionarUsuario(self, codigo, nome):
        if self.arvore.buscar(codigo) is not None:
            return False, "Este ID já está em uso. Por favor, escolha outro."

        string = f"{codigo};{nome};"
        posicao = self.arquivo.gravarRegistro(string)
        self.arvore.inserir(codigo, posicao)

        return True, "Conta criada com sucesso!"

    def buscarUsuario(self, codigo):
        noEncnotrado = self.arvore.buscar(codigo)

        if noEncnotrado is not None:
            linha = self.arquivo.lerRegistro(noEncnotrado.posicaoArquivo)
            dados = linha.strip().split(";")

            if len(dados) == 3:
                progresso = {}

                if dados[2]:
                    for d in dados[2].split('|'):
                        if d:
                            idIdioma, nivel, xp = d.split(':')
                            progresso[int(idIdioma) if idIdioma.isdigit() else 0] = {
                                "nivel": int(nivel) if nivel.isdigit() else 1,
                                "pontuacao": int(xp) if xp.isdigit() else 0}

                return {
                    "codigo": int(dados[0]) if dados[0].isdigit() else 0,
                    "nome": dados[1],
                    "progresso": progresso
                }
            return None

    def excluirUsuario(self, codigo):

        noEncontrado = self.arvore.buscar(codigo)

        if noEncontrado is None:
            print(f"Código informardo ({codigo}) não existe")
            return

        self.arquivo.excluirRegistro(noEncontrado.posicaoArquivo)
        self.arvore.excluirNo(codigo)

        print("Idioma deletado com sucesso!")

    def atualizarStatus(self, codigo, codIdioma, novoNivel, novaPontuacao):
        noEncontrado = self.arvore.buscar(codigo)
        usuarioAntigo = self.buscarUsuario(codigo)

        if noEncontrado is not None and usuarioAntigo is not None:
            self.arquivo.excluirRegistro(noEncontrado.posicaoArquivo)

            usuarioAntigo['progresso'][codIdioma] = {"nivel": novoNivel, "pontuacao": novaPontuacao}

            progressoString = []
            for idIdioma, dadosProgresso in usuarioAntigo['progresso'].items():
                progressoString.append(f"{idIdioma}:{dadosProgresso['nivel']}:{dadosProgresso['pontuacao']}")

            progressoStringFinal = "|".join(progressoString)

            string = f"{codigo};{usuarioAntigo['nome']};{progressoStringFinal}"
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
