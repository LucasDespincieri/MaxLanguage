import customtkinter as ctk


class TelaIdioma(ctk.CTkFrame):
    def __init__(self, master, app_router):
        super().__init__(master, fg_color="transparent")
        self.app_router = app_router

        ctk.CTkLabel(self, text="O que vamos", font=ctk.CTkFont(size=20), text_color="gray").pack(pady=(80, 0))
        ctk.CTkLabel(self, text="aprender hoje?", font=ctk.CTkFont(size=32, weight="bold")).pack(pady=(0, 40))

        idiomasDisponiveis = self.app_router.tabelaIdioma.listarTodosIdiomas()

        if not idiomasDisponiveis:
            ctk.CTkLabel(self, text="Nenhum idioma cadastrado.", text_color="red").pack()

        for idioma in idiomasDisponiveis:
            ctk.CTkButton(
                self,
                text=f"📚 {idioma['nome']}",
                width=250, height=60, font=ctk.CTkFont(size=20, weight="bold"),
                command=lambda cod=idioma['codigo']: self.escolherEAvancar(cod)
            ).pack(pady=10)

        ctk.CTkButton(self, text="Sair", fg_color="transparent", text_color="gray",
                      command=self.app_router.abrirTelaLogin).pack(pady=40)

    def escolherEAvancar(self, codIdioma):
        self.app_router.idiomaAtivo = codIdioma
        self.app_router.abrirPainelAluno()
