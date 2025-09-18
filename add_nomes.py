nomes = []
while True:
    novo_nome = input("digite um nome para adicionar a lista(ou 'sair' para terminar): ")
    if novo_nome.lower() == 'sair' :
        break
    nomes.append(novo_nome)
    print(f"'{novo_nome}' foi adicionado a lista. ")
print("\n--- Nomes na sua lista ---")
for nome in nomes:
    print(nome)
                
