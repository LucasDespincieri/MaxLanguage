import customtkinter as ctk


class TelaAdmin(ctk.CTkFrame):
    def __init__(self, master, app_router):
        super().__init__(master, fg_color="transparent")
        self.app_router = app_router

        ctk.CTkLabel(self, text="Painel do Professor", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(20, 10))

        self.abas = ctk.CTkTabview(self, width=320, height=450)
        self.abas.pack(padx=20, pady=10, fill="both", expand=True)

        self.abaIdioma = self.abas.add("Idioma")
        self.abaLicao = self.abas.add("Lição")
        self.abaExercicio = self.abas.add("Exercício")

        self.setupAbaIdioma()
        self.setupAbaLicao()
        self.setupAbaExercicio()

        ctk.CTkButton(self, text="Sair do Modo Admin", fg_color="transparent", text_color="gray",
                      command=self.app_router.abrirTelaLogin).pack(pady=10)

    def setupAbaIdioma(self):
        ctk.CTkLabel(self.abaIdioma, text="Cadastrar Novo Idioma", font=ctk.CTkFont(weight="bold")).pack(pady=10)

        frame = ctk.CTkFrame(self.abaIdioma, fg_color="transparent")
        frame.pack(pady=10)
        ctk.CTkLabel(frame, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entCodIdioma = ctk.CTkEntry(frame, width=120)
        self.entCodIdioma.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame, text="Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entNomeIdioma = ctk.CTkEntry(frame, width=120)
        self.entNomeIdioma.grid(row=1, column=1, padx=5, pady=5)

        self.lblMsgIdioma = ctk.CTkLabel(self.abaIdioma, text="")
        self.lblMsgIdioma.pack()

        ctk.CTkButton(self.abaIdioma, text="Salvar Idioma", command=self.salvarIdioma).pack(pady=10)

    def salvarIdioma(self):
        codigo = self.entCodIdioma.get()
        nome = self.entNomeIdioma.get()
        if codigo.isdigit() and nome:
            self.app_router.tabelaIdioma.adicionarIdioma(int(codigo), nome)
            self.lblMsgIdioma.configure(text=f"Idioma '{nome}' cadastrado!", text_color="green")
            self.entCodIdioma.delete(0, 'end')
            self.entNomeIdioma.delete(0, 'end')
        else:
            self.lblMsgIdioma.configure(text="Preencha tudo corretamente.", text_color="red")

    def setupAbaLicao(self):
        ctk.CTkLabel(self.abaLicao, text="Cadastrar Nova Lição", font=ctk.CTkFont(weight="bold")).pack(pady=10)

        scroll = ctk.CTkScrollableFrame(self.abaLicao, fg_color="transparent")
        scroll.pack(fill="both", expand=True)

        ctk.CTkLabel(scroll, text="Código da Lição:").pack(anchor="w")
        self.entCodLicao = ctk.CTkEntry(scroll, width=200)
        self.entCodLicao.pack(pady=5)

        ctk.CTkLabel(scroll, text="Título:").pack(anchor="w")
        self.entTitLicao = ctk.CTkEntry(scroll, width=200)
        self.entTitLicao.pack(pady=5)

        ctk.CTkLabel(scroll, text="Cód. Idioma Pertencente:").pack(anchor="w")
        self.entCodIdiomaLicao = ctk.CTkEntry(scroll, width=200)
        self.entCodIdiomaLicao.pack(pady=5)

        ctk.CTkLabel(scroll, text="Total de Níveis:").pack(anchor="w")
        self.entTotalNiveis = ctk.CTkEntry(scroll, width=200)
        self.entTotalNiveis.pack(pady=5)

        self.lblMsgLicao = ctk.CTkLabel(scroll, text="")
        self.lblMsgLicao.pack()

        ctk.CTkButton(scroll, text="Salvar Lição", command=self.salvarLicao).pack(pady=10)

    def salvarLicao(self):
        codigo = self.entCodLicao.get()
        titulo = self.entTitLicao.get()
        codIdioma = self.entCodIdiomaLicao.get()
        niveis = self.entTotalNiveis.get()

        if codigo.isdigit() and titulo and codIdioma.isdigit() and niveis.isdigit():
            self.app_router.tabelaLicao.adicionarLicao(int(codigo), titulo, int(codIdioma), int(niveis))
            self.lblMsgLicao.configure(text=f"Lição '{titulo}' cadastrada!", text_color="green")
            self.entCodLicao.delete(0, 'end')
            self.entTitLicao.delete(0, 'end')
            self.entCodIdiomaLicao.delete(0, 'end')
            self.entTotalNiveis.delete(0, 'end')
        else:
            self.lblMsgLicao.configure(text="Preencha tudo corretamente.", text_color="red")

    def setupAbaExercicio(self):
        ctk.CTkLabel(self.abaExercicio, text="Cadastrar Novo Exercício", font=ctk.CTkFont(weight="bold")).pack(pady=10)

        scroll = ctk.CTkScrollableFrame(self.abaExercicio, fg_color="transparent")
        scroll.pack(fill="both", expand=True)

        ctk.CTkLabel(scroll, text="Cód. Exercício:").pack(anchor="w")
        self.entCodEx = ctk.CTkEntry(scroll, width=200)
        self.entCodEx.pack(pady=5)

        ctk.CTkLabel(scroll, text="Cód. Lição Pertencente:").pack(anchor="w")
        self.entCodLicEx = ctk.CTkEntry(scroll, width=200)
        self.entCodLicEx.pack(pady=5)

        ctk.CTkLabel(scroll, text="Nível de Dificuldade:").pack(anchor="w")
        self.entNivEx = ctk.CTkEntry(scroll, width=200)
        self.entNivEx.pack(pady=5)

        ctk.CTkLabel(scroll, text="Tipo (1=Alt, 2=Texto, 3=Ligar):").pack(anchor="w")
        self.entTipoEx = ctk.CTkEntry(scroll, width=200)
        self.entTipoEx.pack(pady=5)

        ctk.CTkLabel(scroll, text="Descrição / Pergunta:").pack(anchor="w")
        self.entDescEx = ctk.CTkEntry(scroll, width=200)
        self.entDescEx.pack(pady=5)

        ctk.CTkLabel(scroll, text="Opções (separadas por '|'):").pack(anchor="w")
        self.entOpcEx = ctk.CTkEntry(scroll, width=200)
        self.entOpcEx.pack(pady=5)

        ctk.CTkLabel(scroll, text="Resposta Correta:").pack(anchor="w")
        self.entRespEx = ctk.CTkEntry(scroll, width=200)
        self.entRespEx.pack(pady=5)

        ctk.CTkLabel(scroll, text="XP (Pontuação):").pack(anchor="w")
        self.entXpEx = ctk.CTkEntry(scroll, width=200)
        self.entXpEx.pack(pady=5)

        self.lblMsgEx = ctk.CTkLabel(scroll, text="")
        self.lblMsgEx.pack()

        ctk.CTkButton(scroll, text="Salvar Exercício", command=self.salvarExercicio).pack(pady=10)

    def salvarExercicio(self):
        cod = self.entCodEx.get()
        codLic = self.entCodLicEx.get()
        niv = self.entNivEx.get()
        tipo = self.entTipoEx.get()
        desc = self.entDescEx.get()
        opcoes = self.entOpcEx.get()
        resp = self.entRespEx.get()
        xp = self.entXpEx.get()

        if cod.isdigit() and codLic.isdigit() and niv.isdigit() and tipo.isdigit() and xp.isdigit() and desc and resp:
            self.app_router.tabelaExercicio.adicionarExercicio(
                int(cod), int(codLic), int(niv), int(tipo), desc, opcoes, resp, int(xp)
            )
            self.lblMsgEx.configure(text=f"Exercício cadastrado!", text_color="green")
            for ent in [self.entCodEx, self.entCodLicEx, self.entNivEx, self.entTipoEx, self.entDescEx, self.entOpcEx,
                        self.entRespEx, self.entXpEx]:
                ent.delete(0, 'end')
        else:
            self.lblMsgEx.configure(text="Preencha tudo corretamente.", text_color="red")
