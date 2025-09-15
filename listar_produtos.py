def listar_produtos():
    produto1 ="computador"
    produto2 = "mesa de escritorio"

    idade = 30
    codigo = 5290
    genero = 'M'

    preco1 = 2100.0
    preco2 = 650.50
    medida = 53.234567

    print("produtos:")
    print(f"{produto1}, cujo preço é $ {preco1:,.2f}")
    print(f"{produto2}, cujo preço é $ {preco2:,.2f}")


    print(f"Registro: {idade} anos de idade, código {codigo} e gênero {genero}")

    print()
    print(f"Medida com oito casas decimais: {medida:.8f}")
    print(f"Arredondado (três casas decimais): {medida:.3f}")

    print(f"Separador decimal invariant culture: {medida:.3f}".replace(",", "."))