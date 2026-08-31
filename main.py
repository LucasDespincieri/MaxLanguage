import customtkinter as ctk

# Configuração básica de tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criação da janela principal
janela = ctk.CTk()
janela.geometry("400x300")
janela.title("MaxLanguage - Teste GUI")

# Adicionando um elemento na tela
label = ctk.CTkLabel(janela, text="CustomTkinter rodando com sucesso!", font=("Arial", 16))
label.pack(pady=100)

# Mantém a janela aberta
janela.mainloop()