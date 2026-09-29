import customtkinter as ctk


class TelaAdmin(ctk.CTkFrame):
    def __init__(self, master, app_router):
        super().__init__(master, fg_color="transparent")
        self.app_router = app_router

        ctk.CTkLabel(self, text="Painel do Professor", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(40, 20))

        formFrame = ctk.CTkFrame(self)
        formFrame.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(formFrame, text="Cadastrar Novo Idioma", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0,
                                                                                                    columnspan=2,
                                                                                                    pady=10)

        ctk.CTkLabel(formFrame, text="Código:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entradaCod = ctk.CTkEntry(formFrame, width=150)
        self.entradaCod.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(formFrame, text="Nome:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entradaNome = ctk.CTkEntry(formFrame, width=150)
        self.entradaNome.grid(row=2, column=1, padx=10, pady=10)

        self.lblMsg = ctk.CTkLabel(formFrame, text="", text_color="green")
        self.lblMsg.grid(row=3, column=0, columnspan=2)

        btnSalvar = ctk.CTkButton(formFrame, text="Salvar Idioma", command=self.salvarIdioma)
        btnSalvar.grid(row=4, column=0, columnspan=2, pady=15)

        ctk.CTkButton(self, text="Sair do Modo Admin", fg_color="transparent", text_color="gray",
                      command=self.app_router.abrirTelaLogin).pack(pady=40)

    def salvarIdioma(self):
        codigo = self.entradaCod.get()
        nome = self.entradaNome.get()

        if codigo.isdigit() and nome:
            self.app_router.tabelaIdioma.adicionarIdioma(int(codigo), nome)
            self.lblMsg.configure(text=f"Idioma '{nome}' cadastrado!", text_color="green")
            self.entradaCod.delete(0, 'end')
            self.entradaNome.delete(0, 'end')
        else:
            self.lblMsg.configure(text="Erro: Preencha todos os campos corretamente.", text_color="red")
