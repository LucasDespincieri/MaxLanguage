import customtkinter as ctk


class TelaLogin(ctk.CTkFrame):
    def __init__(self, master, app_router):
        super().__init__(master, fg_color="transparent")
        self.app_router = app_router

        titulo = ctk.CTkLabel(self, text="MaxLanguage", font=ctk.CTkFont(size=32, weight="bold"))
        titulo.pack(pady=(100, 10))

        subtitulo = ctk.CTkLabel(self, text="Aprenda jogando.", font=ctk.CTkFont(size=16), text_color="gray")
        subtitulo.pack(pady=(0, 40))

        self.entradaCodigo = ctk.CTkEntry(self, placeholder_text="Digite seu ID de usuário", width=250, height=45)
        self.entradaCodigo.pack(pady=10)

        self.labelErro = ctk.CTkLabel(self, text="", text_color="red")
        self.labelErro.pack()

        btnEntrar = ctk.CTkButton(self, text="ENTRAR", width=250, height=45, font=ctk.CTkFont(weight="bold"),
                                  command=self.fazerLogin)
        btnEntrar.pack(pady=10)

        # NOVO: Botão para Criar Conta
        btnCriarConta = ctk.CTkButton(self, text="Criar Nova Conta", fg_color="transparent", text_color="#58CC02",
                                      border_width=2, border_color="#58CC02", width=250, height=45,
                                      command=self.app_router.abrirTelaRegistro)
        btnCriarConta.pack(pady=10)

        btnAdmin = ctk.CTkButton(self, text="Área do Professor", fg_color="transparent", text_color="gray",
                                 command=self.app_router.abrirPainelAdmin)
        btnAdmin.pack(pady=20)

    def fazerLogin(self):
        codigoDigitado = self.entradaCodigo.get()

        if not codigoDigitado.isdigit():
            self.labelErro.configure(text="O código deve ser um número!")
            return

        usuario = self.app_router.tabelaUsuario.buscarUsuario(int(codigoDigitado))

        if usuario:
            self.app_router.usuarioLogado = usuario
            self.app_router.abrirSelecaoIdioma()
        else:
            self.labelErro.configure(text="Usuário não encontrado!")
