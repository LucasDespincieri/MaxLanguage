from model.Gerenciador import Gerenciador
from model.ArvoreBinaria import ArvoreBinaria

class Idioma:

  def __init__(self):

      self.arvore = ArvoreBinaria()
      self.arquivo = Gerenciador("idioma.txt")
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


  def adicionarIdioma(self, codigo, nome):
      linhaString = f"{codigo};{nome}"

      posicao = self.arquivo.gravarRegistro(linhaString)
      self.arvore.inserir(codigo,posicao)
      print(f"Idioma {nome} adicionado")

  def buscarIdioma(self,codigo):

      noEncontrado = self.arvore.buscar(codigo)

      if noEncontrado is not None:
          linha = self.arquivo.lerRegistro(noEncontrado.posicaoArquivo)

          dados = linha.split(';')
          if len(dados) == 2:
              return {"codigo": int(dados[0]), "nome": dados[1]}

      return None