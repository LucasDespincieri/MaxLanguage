import os


class Gerenciador:
    def __init__(self, nomeArquivo):

        self.caminhoArquivo = f"data/{nomeArquivo}"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.caminhoArquivo):
            open(self.caminhoArquivo, 'w').close()

    def gravarRegistro(self, dado):
        pass

