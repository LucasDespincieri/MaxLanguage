class GameController:
    def __init__(self, tabelaUsuario, tabelaExercicio, tabelaLicao):
        self.tabelaUsuario = tabelaUsuario
        self.tabelaExercicio = tabelaExercicio
        self.tabelaLicao = tabelaLicao

    def praticar(self, codUsuario, codIdioma, codExercicio, respostaDada):
        usuario = self.tabelaUsuario.buscarUsuario(codUsuario)
        exercicio = self.tabelaExercicio.buscarExercicio(codExercicio)

        if not usuario:
            return "Erro: Usuário não encontrado."
        if not exercicio:
            return "Erro: Exercício não encontrado."

        progressoAtual = usuario['progresso'].get(codIdioma, {"nivel": 1, "pontuacao": 0})
        nivelAtual = progressoAtual['nivel']
        pontosAtuais = progressoAtual['pontuacao']

        if exercicio['nivelDificuldade'] > nivelAtual:
            return f"Bloqueado! Este exercício é Nível {exercicio['nivelDificuldade']}, mas você é Nível {nivelAtual} neste idioma."

        if respostaDada.lower().strip() == exercicio['respostaCorreta'].lower().strip():
            pontosAtuais += exercicio['pontuacao']
            mensagem = f"Parabéns! Você acertou e ganhou {exercicio['pontuacao']} XP."
        else:
            penalidade = int(exercicio['pontuacao'] * 0.10)
            pontosAtuais -= penalidade
            if pontosAtuais < 0: pontosAtuais = 0
            mensagem = f"Resposta incorreta. A resposta era '{exercicio['respostaCorreta']}'. Você perdeu {penalidade} XP."

        if pontosAtuais >= 100:
            nivelAtual += 1
            pontosAtuais -= 100
            mensagem += f"\n🎉 LEVEL UP! Você subiu para o Nível {nivelAtual}!"

        totalNiveis = 5

        if nivelAtual > totalNiveis:
            mensagem = "Parabéns! Você terminou todas as lições e garantiu seu certificado de proficiência!"
            self.tabelaUsuario.atualizarStatus(codUsuario, codIdioma, nivelAtual, pontosAtuais)
            return mensagem

        self.tabelaUsuario.atualizarStatus(codUsuario, codIdioma, nivelAtual, pontosAtuais)
        return mensagem

    def gerarRankingPorIdioma(self, codIdioma, nomeIdioma):
        usuarios = self.tabelaUsuario.listarTodosUsuarios()

        if not usuarios:
            return []

        usuariosIdioma = []
        for usuario in usuarios:
            # Pega o progresso do usuário no idioma específico
            progresso = usuario.get('progresso', {}).get(codIdioma)
            if progresso:
                xpTotal = (progresso['nivel'] - 1) * 100 + progresso['pontuacao']
                usuariosIdioma.append({
                    'nome': usuario['nome'],
                    'xp_total': xpTotal
                })

        usuariosIdioma.sort(key=lambda x: x['xp_total'], reverse=True)

        return usuariosIdioma
