import os

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

if __name__ == "__main__":
    # nome = input("Digite o nome do arquivo ou pasta que deseja buscar: ") C:\Users\ricardo.pereira\Documents\teste
    nome = "index"
    resultados = buscar(nome, r"C:\\Users\\ricardo.pereira\Documents\\pasta dev\\front")  # ou "/home" no Linux

    if resultados:
        print("Foram encontrados:\n")
        with open("output.txt", "w") as  arquivo:
            for r in resultados:
                resultadoTratado = r.replace("\\\\", "\\")
                arquivo.write(f"\n\{resultadoTratado}")
                print(f"\{resultadoTratado}")
    else:
        print("Nenhum resultado encontrado.")