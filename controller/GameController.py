class GameController:
    def __init__(self, tabelaUsuario, tabelaExercicio, tabelaLicao):
        self.tabelaUsuario = tabelaUsuario
        self.tabelaExercicio = tabelaExercicio
        self.tabelaLicao = tabelaLicao

    def praticar(self, codUsuario, codExercicio, respostaDada):
        usuario = self.tabelaUsuario.buscarUsuario(codUsuario)
        exercicio = self.tabelaExercicio.buscarExercicio(codExercicio)

        if not usuario:
            return "Erro: Usuário não encontrado."
        if not exercicio:
            return "Erro: Exercício não encontrado."

        if exercicio['nivelDificuldade'] > usuario['nivel']:
            return f"Bloqueado! Este exercício é Nível {exercicio['nivelDificuldade']}, mas você é Nível {usuario['nivel']}."

        nivelAtual = usuario['nivel']
        pontosAtuais = usuario['pontuacao']

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
            mensagem = f"Prabéns! Você terminou todas as lições e garantiu seu certificado de proficiência em {exercicio['descricao']}"
            self.tabelaUsuario.atualizarStatus(codUsuario, nivelAtual, pontosAtuais)
            return mensagem

        self.tabelaUsuario.atualizarStatus(codUsuario, nivelAtual, pontosAtuais)
        return mensagem

    def gerarRanking(self):
        usuarios = self.tabelaUsuario.listarTodosUsuarios()

        if not usuarios:
            return "Nenhum usuário cadastrado no momento."

        usuarios.sort(key=lambda u: u['pontuacao'], reverse=True)

        ranking_formatado = "\n🏆 --- RANKING MAXLANGUAGE --- 🏆\n"
        for posicao, usuario in enumerate(usuarios, start=1):
            ranking_formatado += f"{posicao}º Lugar | {usuario['nome']} - Nível {usuario['nivel']} com {usuario['pontuacao']} XP\n"

        return ranking_formatado