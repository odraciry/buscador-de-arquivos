import os
import customtkinter as ctk

# Função para abrir nova janela
def abrir_nova_janela(resultados):
    nova_janela = ctk.CTkToplevel(app)  # ⬅️ cria uma nova janela ligada à principal
    nova_janela.geometry("600x300")
    nova_janela.title("Nova Tela")
    nova_janela.attributes("-topmost", True)
    label = ctk.CTkLabel(nova_janela, text="CAMINHOS DAS PASTAS E ARQUIVOS ENCONTRADOS")
    label.pack(pady=20)

    textbox = ctk.CTkTextbox(nova_janela, width=550, height=150)
    textbox.pack(pady=2)
    # Adiciona texto
    # textbox.insert("0.0", "Aqui está um texto grande que você pode selecionar e copiar!")
    contador = 0
    if(len(resultados) < 1):
         textbox.insert("end", f"nenhum resultado encontrado")
    else:
        for resultado in resultados:
            contador += 1
            # Adiciona texto
            textbox.insert("end", f"{contador} - {resultado}\n\n")
    contador = 0
        
    botao_fechar = ctk.CTkButton(nova_janela, text="Fechar", command=nova_janela.destroy)
    botao_fechar.pack(pady=10)

def buscar(nomeBusca, caminhoInicial):
    resultados = []

    for raiz, dirs, arquivos in os.walk(caminhoInicial):
        print(f"\n PASTA ATUAL: {raiz}")
        print(f"\nSUBPASTAS: {dirs}")
        print(f"\nARQUIVOS: {arquivos}")
        for nome in arquivos + dirs:
            if nomeBusca.lower().replace(".png", "").replace(".jpg", "").replace(".jpeg", "") in nome.lower().replace(".png", "").replace(".jpg", "").replace(".jpeg", ""):
                resultados.append(os.path.join(raiz, nome))
   
    return resultados

# if __name__ == "__main__":
#     # nome = input("Digite o nome do arquivo ou pasta que deseja buscar: ") C:\Users\ricardo.pereira\Documents\teste
#     nome = "P2-B_user_pt-BR_3.1.39_1223_20240308074738"
#     # resultados = buscar(nome, r"\\172.16.17.18\\depto\\Automacao-Rep\\Android\\")  # ou "/home" no Linux
#     resultados = buscar(nome, r"C:\\Users\\ricardo.pereira\\Documents")  # ou "/home" no Linux

#     if resultados:
#         print("Foram encontrados:\n")
#         with open("output.txt", "w") as  arquivo:
#             for r in resultados:
#                 resultadoTratado = r.replace("\\\\", "\\")
#                 arquivo.write(f"\n\{resultadoTratado}")
#                 print(f"\{resultadoTratado}")
#     else:
#         print("Nenhum resultado encontrado.")


def btBuscar(nome_arquivo, caminho):
    resultados = buscar(nome_arquivo, caminho)  # ou "/home" no Linux

    print("Foram encontrados:\n")
    with open("output.txt", "w") as  arquivo:
        for r in resultados:
            resultadoTratado = r.replace("\\\\", "\\")
            arquivo.write(f"\n\{resultadoTratado}")
            print(f"{resultadoTratado}")
    abrir_nova_janela(resultados)
    

# Define o modo de aparência
ctk.set_appearance_mode("dark")  # "light" ou "system"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

# Janela principal
app = ctk.CTk()  
app.title("SEARCH ENGINE")
app.geometry("500x200")

# Widgets modernos
label = ctk.CTkLabel(app, text="Preencha os campos para buscar", font=("Arial", 16))
label.pack(pady=2)

entradaCaminho = ctk.CTkEntry(app, placeholder_text="Caminho inicial (C:\\Users\\ricardo.pereira\\)", width=300)
entradaCaminho.pack(pady=10)

entradaNomeArquivo = ctk.CTkEntry(app, placeholder_text="Nome do arquivo (arquivo.jpg ou nome_pasta)", width=300)
entradaNomeArquivo.pack(pady=10)

botao = ctk.CTkButton(app, text="BUSCAR", command=lambda: btBuscar(entradaNomeArquivo.get(), entradaCaminho.get()))
botao.pack(pady=10)

app.mainloop()

