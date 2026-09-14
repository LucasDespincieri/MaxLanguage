from model.Idioma import Idioma

tabela = Idioma()

tabela.adicionarIdioma(1, "Inglês")
tabela.adicionarIdioma(5, "Espanhol")
tabela.adicionarIdioma(3, "Japonês")

print("\n--- Teste de Busca ---")
codigo = 3
resultado = tabela.buscarIdioma(codigo)

if resultado:
    print(f"Idioma encontrado! Código: {resultado['codigo']} | Descrição: {resultado['nome']}")
else:
    print("Idioma não existe.")

tabela.deletarIdioma(5)

