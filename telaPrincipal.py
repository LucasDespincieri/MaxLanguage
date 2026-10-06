import customtkinter as ctk
from model.Idioma import Idioma
from model.Licao import Licao
from model.Exercicio import Exercicio
from model.Usuario import Usuario
from controller.GameController import GameController

from view.telaLogin import TelaLogin
from view.telaIdioma import TelaIdioma
from view.telaMapaAluno import TelaMapaAluno
from view.telaAdmin import TelaAdmin
from view.telaRegistro import TelaRegistro

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class MaxLanguageApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MaxLanguage")
        self.geometry("360x700")
        self.resizable(False, False)

        # Banco de Dados
        self.tabelaIdioma = Idioma()
        self.tabelaLicao = Licao(self.tabelaIdioma)
        self.tabelaExercicio = Exercicio(self.tabelaLicao, self.tabelaIdioma)
        self.tabelaUsuario = Usuario(self.tabelaIdioma)
        self.gameController = GameController(self.tabelaUsuario, self.tabelaExercicio, self.tabelaLicao)

        # Estados globais
        self.usuarioLogado = None
        self.idiomaAtivo = None
        self.frameAtual = None

        self.abrirTelaLogin()

    def limparTela(self):
        if self.frameAtual is not None:
            self.frameAtual.destroy()

    def abrirTelaLogin(self):
        self.limparTela()
        self.frameAtual = TelaLogin(master=self, app_router=self)
        self.frameAtual.pack(fill="both", expand=True)

    def abrirSelecaoIdioma(self):
        self.limparTela()
        self.frameAtual = TelaIdioma(master=self, app_router=self)
        self.frameAtual.pack(fill="both", expand=True)

    def abrirPainelAluno(self):
        self.limparTela()
        self.frameAtual = TelaMapaAluno(master=self, app_router=self)
        self.frameAtual.pack(fill="both", expand=True)

    def abrirPainelAdmin(self):
        self.limparTela()
        self.frameAtual = TelaAdmin(master=self, app_router=self)
        self.frameAtual.pack(fill="both", expand=True)

    def abrirTelaRegistro(self):
        self.limparTela()
        self.frameAtual = TelaRegistro(master=self, app_router=self)
        self.frameAtual.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = MaxLanguageApp()
    app.mainloop()
