import customtkinter as ctk


class TelaRegistro(ctk.CTkFrame):
    def __init__(self, master, app_router):
        super().__init__(master, fg_color="transparent")
        self.app_router = app_router

        titulo = ctk.CTkLabel(self, text="Nova Conta", font=ctk.CTkFont(size=32, weight="bold"))
        titulo.pack(pady=(80, 10))

        subtitulo = ctk.CTkLabel(self, text="Crie o seu perfil de estudante.", font=ctk.CTkFont(size=16),
                                 text_color="gray")
        subtitulo.pack(pady=(0, 40))

        self.entradaNome = ctk.CTkEntry(self, placeholder_text="Digite o seu Nome", width=250, height=45)
        self.entradaNome.pack(pady=10)

        self.entradaId = ctk.CTkEntry(self, placeholder_text="Escolha um ID (apenas números)", width=250, height=45)
        self.entradaId.pack(pady=10)

        self.lblMsg = ctk.CTkLabel(self, text="", text_color="green", wraplength=280)
        self.lblMsg.pack(pady=5)

        btnRegistrar = ctk.CTkButton(self, text="REGISTAR", width=250, height=45, font=ctk.CTkFont(weight="bold"),
                                     command=self.fazerRegistro)
        btnRegistrar.pack(pady=15)

        btnVoltar = ctk.CTkButton(self, text="Voltar ao Login", fg_color="transparent", text_color="gray",
                                  command=self.app_router.abrirTelaLogin)
        btnVoltar.pack(pady=10)

    def fazerRegistro(self):
        nome = self.entradaNome.get().strip()
        id_str = self.entradaId.get().strip()

        if not nome or not id_str:
            self.lblMsg.configure(text="Preencha todos os campos!", text_color="red")
            return

        if not id_str.isdigit():
            self.lblMsg.configure(text="O ID deve conter apenas números!", text_color="red")
            return

        codigoDesejado = int(id_str)

        sucesso, msg = self.app_router.tabelaUsuario.adicionarUsuario(codigoDesejado, nome)

        if sucesso:
            self.lblMsg.configure(text=f"Conta criada com sucesso! Faça login com o ID {codigoDesejado}.",
                                  text_color="green", font=ctk.CTkFont(weight="bold"))
            self.entradaNome.delete(0, 'end')
            self.entradaId.delete(0, 'end')
        else:
            self.lblMsg.configure(text=msg, text_color="red", font=ctk.CTkFont(weight="normal"))
