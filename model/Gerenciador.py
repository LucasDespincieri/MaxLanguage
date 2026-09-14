import os

class Gerenciador:

    def __init__(self, nomeArquivo):

        self.caminhoArquivo = f"data/{nomeArquivo}"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.caminhoArquivo):
            open(self.caminhoArquivo, 'w').close()

    def gravarRegistro(self, dado):
        with open(self.caminhoArquivo, 'a', encoding='utf-8') as arquivo:
            posicao = arquivo.tell()
            arquivo.write(dado + '\n')
            return posicao

    def lerRegistro(self, posicao):
        with open(self.caminhoArquivo, 'r', encoding='utf-8') as arquivo:
            arquivo.seek(posicao)
            linha = arquivo.readline()
            return linha.strip()

    def excluirRegistro(self, posicao):
        with open(self.caminhoArquivo, 'r+', encoding='utf-8') as arquivo:
            arquivo.seek(posicao)
            arquivo.write("#")
