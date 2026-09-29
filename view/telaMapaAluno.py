import customtkinter as ctk


class TelaMapaAluno(ctk.CTkFrame):
    def __init__(self, master, app_router):
        super().__init__(master, fg_color="transparent")
        self.app_router = app_router
        self.desenharMapa()

    def limparFrame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def desenharMapa(self):
        self.limparFrame()
        usuario = self.app_router.usuarioLogado
        idiomaAtual = self.app_router.idiomaAtivo

        progresso = usuario['progresso'].get(idiomaAtual, {"nivel": 1, "pontuacao": 0})
        nivelAtualUsuario = progresso['nivel']
        pontuacaoAtual = progresso['pontuacao']

        frameStatus = ctk.CTkFrame(self, height=60, corner_radius=0)
        frameStatus.pack(fill="x", side="top")

        ctk.CTkLabel(frameStatus, text=f"👤 {usuario['nome']}", font=ctk.CTkFont(size=16, weight="bold")).pack(
            side="left", padx=15, pady=15)

        ctk.CTkLabel(frameStatus, text=f"⭐ Nível {nivelAtualUsuario} | ⚡ {pontuacaoAtual} XP",
                     font=ctk.CTkFont(size=14)).pack(side="right", padx=15, pady=15)

        btnRanking = ctk.CTkButton(frameStatus, text="🏆 Ranking", width=100, command=self.mostrarRanking)
        btnRanking.pack(side="right", padx=15, pady=15)

        mapaFrame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        mapaFrame.pack(fill="both", expand=True)

        licoesDoIdioma = self.app_router.tabelaLicao.listarLicoesPorIdioma(idiomaAtual)

        nivelGlobal = 1
        deslocamentosX = [0, 60, 0, -60]

        for indexLicao, licao in enumerate(licoesDoIdioma, start=1):
            frameUnidade = ctk.CTkFrame(mapaFrame, fg_color="#58CC02", corner_radius=15)
            frameUnidade.pack(fill="x", padx=20, pady=(20, 10))

            ctk.CTkLabel(frameUnidade, text=f"Unidade {indexLicao}", font=ctk.CTkFont(size=22, weight="bold"),
                         text_color="white").pack(anchor="w", padx=20, pady=(15, 0))
            ctk.CTkLabel(frameUnidade, text=licao['titulo'], font=ctk.CTkFont(size=14), text_color="white").pack(
                anchor="w", padx=20, pady=(0, 15))

            for dificuldadeInterna in range(1, licao['totalNiveis'] + 1):
                isDesbloqueado = nivelGlobal <= nivelAtualUsuario
                isAtual = nivelGlobal == nivelAtualUsuario

                corFundo = "#58CC02" if isDesbloqueado else "#E5E5E5"
                corHover = "#46A302" if isDesbloqueado else "#E5E5E5"
                corTexto = "white" if isDesbloqueado else "#AFAFAF"

                if isAtual:
                    textoBotao = "★"
                elif isDesbloqueado:
                    textoBotao = "✔"
                else:
                    textoBotao = "🔒"

                linha = ctk.CTkFrame(mapaFrame, fg_color="transparent")
                linha.pack(fill="x", pady=15)

                btnFase = ctk.CTkButton(
                    linha, text=textoBotao, width=75, height=75, corner_radius=40,
                    font=ctk.CTkFont(size=28, weight="bold"),
                    fg_color=corFundo, hover_color=corHover, text_color=corTexto,
                    state="normal" if isDesbloqueado else "disabled",
                    command=lambda l=licao['codigo'], d=dificuldadeInterna: self.iniciarPratica(l, d)
                )

                margem = deslocamentosX[(nivelGlobal - 1) % 4]
                if margem > 0:
                    btnFase.pack(padx=(margem, 0))
                elif margem < 0:
                    btnFase.pack(padx=(0, abs(margem)))
                else:
                    btnFase.pack()
                nivelGlobal += 1

        btnSair = ctk.CTkButton(mapaFrame, text="Trocar de Idioma", width=200, fg_color="transparent", border_width=2,
                                text_color="gray", command=self.app_router.abrirSelecaoIdioma)
        btnSair.pack(pady=30)

    def iniciarPratica(self, codLicao, dificuldadeDesejada):
        self.limparFrame()

        exercicioAtual = self.app_router.tabelaExercicio.buscarExercicioPorNivelDificuldade(codLicao,
                                                                                            dificuldadeDesejada)

        if not exercicioAtual:
            ctk.CTkLabel(self, text=f"Nenhum exercício cadastrado para a Lição {codLicao}, Fase {dificuldadeDesejada}!",
                         text_color="red").pack(pady=50)
            ctk.CTkButton(self, text="Voltar ao Mapa", command=self.desenharMapa).pack()
            return

        codigoExercicio = exercicioAtual['codigo']

        frameTop = ctk.CTkFrame(self, fg_color="transparent")
        frameTop.pack(fill="x", padx=20, pady=20)

        ctk.CTkButton(frameTop, text="✖", width=40, height=40, fg_color="transparent", text_color="gray",
                      hover_color="#333333", font=ctk.CTkFont(size=20), command=self.desenharMapa).pack(side="left")

        barraProgresso = ctk.CTkProgressBar(frameTop, width=200, height=15, fg_color="#4B4B4B",
                                            progress_color="#58CC02")
        barraProgresso.pack(side="left", padx=20)
        barraProgresso.set(0.5)

        ctk.CTkLabel(self, text=f"Fase {dificuldadeDesejada}", font=ctk.CTkFont(size=14, weight="bold"),
                     text_color="gray").pack(pady=(20, 0))

        lblPergunta = ctk.CTkLabel(self, text=exercicioAtual['descricao'], font=ctk.CTkFont(size=24, weight="bold"),
                                   wraplength=300)
        lblPergunta.pack(pady=(10, 20))

        tipoExercicio = exercicioAtual.get('tipo', 1)

        if tipoExercicio == 1:
            for opcao in exercicioAtual['opcoes']:
                ctk.CTkButton(
                    self, text=opcao, width=280, height=55, font=ctk.CTkFont(size=18), fg_color="green",
                    border_width=2, border_color="#4B4B4B", hover_color="#333333", anchor="w",
                    command=lambda resp=opcao, cod=codigoExercicio, cL=codLicao,
                                   dD=dificuldadeDesejada: self.verificar_resposta(cod, resp, cL, dD)
                ).pack(pady=8)

        elif tipoExercicio == 2:
            entradaResposta = ctk.CTkEntry(self, width=280, height=45, font=ctk.CTkFont(size=16),
                                           placeholder_text="Digite aqui...")
            entradaResposta.pack(pady=15)

            ctk.CTkButton(
                self, text="VERIFICAR", width=280, height=50, font=ctk.CTkFont(size=16, weight="bold"),
                fg_color="#58CC02",
                command=lambda: self.verificar_resposta(codigoExercicio, entradaResposta.get(), codLicao,
                                                        dificuldadeDesejada)
            ).pack(pady=10)

        elif tipoExercicio == 3:

            import random
            pares = []
            colunaEsq = []
            colunaDir = []

            for par in exercicioAtual['opcoes']:
                if '=' in par:
                    esq, dir = par.split('=')
                    pares.append((esq.strip(), dir.strip()))
                    colunaEsq.append(esq.strip())
                    colunaDir.append(dir.strip())

            random.shuffle(colunaDir)
            comboboxes = []

            for esq in colunaEsq:
                frameLinha = ctk.CTkFrame(self, fg_color="transparent")
                frameLinha.pack(pady=5)
                ctk.CTkLabel(frameLinha, text=esq, width=120, font=ctk.CTkFont(size=16, weight="bold"),
                             anchor="e").pack(side="left", padx=10)

                combo = ctk.CTkComboBox(frameLinha, values=colunaDir, width=150, state="readonly")
                combo.set("Selecione")
                combo.pack(side="left", padx=10)
                comboboxes.append((esq, combo))

            def validarLigar():
                respostas = []
                for esq, combo in comboboxes:
                    respostas.append(f"{esq}={combo.get()}")
                respostaFinal = "|".join(respostas)
                self.verificar_resposta(codigoExercicio, respostaFinal, codLicao, dificuldadeDesejada)

            ctk.CTkButton(
                self, text="VERIFICAR", width=280, height=50, font=ctk.CTkFont(size=16, weight="bold"),
                fg_color="#58CC02",
                command=validarLigar
            ).pack(pady=20)

    def verificar_resposta(self, codExercicio, respostaEscolhida, codLicao, dificuldadeDesejada):
        idiomaAtual = self.app_router.idiomaAtivo

        progressoAntigo = self.app_router.usuarioLogado['progresso'].get(idiomaAtual, {"nivel": 1, "pontuacao": 0})
        nivelAnterior = progressoAntigo['nivel']

        mensagemResultado = self.app_router.gameController.praticar(
            self.app_router.usuarioLogado['codigo'],
            idiomaAtual,
            codExercicio,
            respostaEscolhida
        )

        self.app_router.usuarioLogado = self.app_router.tabelaUsuario.buscarUsuario(
            self.app_router.usuarioLogado['codigo'])

        progressoNovo = self.app_router.usuarioLogado['progresso'].get(idiomaAtual, {"nivel": 1, "pontuacao": 0})
        subiuDeNivel = progressoNovo['nivel'] > nivelAnterior

        isAcerto = "Parabéns" in mensagemResultado or "LEVEL" in mensagemResultado
        corFundo = "#58CC02" if isAcerto else "#FF4B4B"

        popUp = ctk.CTkToplevel(self)
        popUp.title("Resultado")
        popUp.geometry("340x260")
        popUp.resizable(False, False)
        popUp.transient(self)
        popUp.grab_set()

        framePopUp = ctk.CTkFrame(popUp, fg_color=corFundo, corner_radius=0)
        framePopUp.pack(fill="both", expand=True)

        lblMensagem = ctk.CTkLabel(framePopUp, text=mensagemResultado, font=ctk.CTkFont(size=18, weight="bold"),
                                   text_color="white", wraplength=300)
        lblMensagem.pack(pady=(40, 20), padx=20)

        def voltarAoMapa():
            popUp.destroy()
            self.desenharMapa()

        def proximaPergunta():
            popUp.destroy()
            self.iniciarPratica(codLicao, dificuldadeDesejada)

        if subiuDeNivel:
            ctk.CTkButton(framePopUp, text="VOLTAR AO MAPA", width=220, height=45, fg_color="white",
                          text_color=corFundo, font=ctk.CTkFont(size=16, weight="bold"), hover_color="#F0F0F0",
                          command=voltarAoMapa).pack(pady=10)
        else:
            ctk.CTkButton(framePopUp, text="PRÓXIMA PERGUNTA", width=220, height=45, fg_color="white",
                          text_color=corFundo, font=ctk.CTkFont(size=16, weight="bold"), hover_color="#F0F0F0",
                          command=proximaPergunta).pack(pady=(0, 10))
            ctk.CTkButton(framePopUp, text="PARAR POR AGORA", width=220, height=35, fg_color="transparent",
                          text_color="white", font=ctk.CTkFont(size=14, weight="bold"), border_width=2,
                          border_color="white", hover_color=corFundo, command=voltarAoMapa).pack(pady=5)

    def mostrarRanking(self):
        idiomaAtual = self.app_router.idiomaAtivo
        idiomaObjeto = self.app_router.tabelaIdioma.buscarIdioma(idiomaAtual)
        nomeIdioma = idiomaObjeto['nome'] if idiomaObjeto else "Desconhecido"

        ranking_dados = self.app_router.gameController.gerarRankingPorIdioma(idiomaAtual, nomeIdioma)

        popUp = ctk.CTkToplevel(self)
        popUp.title(f"Ranking - {nomeIdioma}")
        popUp.geometry("400x500")
        popUp.resizable(False, False)
        popUp.transient(self)
        popUp.grab_set()

        framePopUp = ctk.CTkFrame(popUp, corner_radius=0)
        framePopUp.pack(fill="both", expand=True)

        lblTitulo = ctk.CTkLabel(framePopUp, text=f"🏆 Ranking: {nomeIdioma} 🏆",
                                 font=ctk.CTkFont(size=20, weight="bold"))
        lblTitulo.pack(pady=(20, 10))

        scrollRanking = ctk.CTkScrollableFrame(framePopUp, width=360, height=360, fg_color="transparent")
        scrollRanking.pack(padx=20, pady=10, fill="both", expand=True)

        if not ranking_dados:
            ctk.CTkLabel(scrollRanking, text="Nenhum usuário possui progresso neste idioma.",
                         font=ctk.CTkFont(size=14)).pack(pady=20)
        else:
            for posicao, usuario in enumerate(ranking_dados, start=1):
                iconePosicao = "🥇" if posicao == 1 else "🥈" if posicao == 2 else "🥉" if posicao == 3 else f"{posicao}º"

                frameItem = ctk.CTkFrame(scrollRanking, fg_color="#58CC02", corner_radius=15)
                frameItem.pack(fill="x", pady=(0, 10))

                lblPos = ctk.CTkLabel(frameItem, text=iconePosicao, font=ctk.CTkFont(size=20, weight="bold"),
                                      text_color="white", width=40)
                lblPos.pack(side="left", padx=(15, 5), pady=15)

                lblNome = ctk.CTkLabel(frameItem, text=usuario['nome'], font=ctk.CTkFont(size=16, weight="bold"),
                                       text_color="white")
                lblNome.pack(side="left", padx=5, pady=15)

                lblXp = ctk.CTkLabel(frameItem, text=f"{usuario['xp_total']} XP",
                                     font=ctk.CTkFont(size=14, weight="bold"), text_color="white")
                lblXp.pack(side="right", padx=15, pady=15)

        ctk.CTkButton(framePopUp, text="Fechar", width=120, command=popUp.destroy).pack(pady=(10, 20))
