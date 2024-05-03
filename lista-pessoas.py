def lista_pessoas():
    soma = 0
    media = 0
    for i in range (5):
        nomes = input(f"Digite o {i+1}ª nome:")
        idades = int(input(f"Digite a {i+1}ª idade:"))
        soma += idades
    media = soma/ 5
    print(f"A soma das idades é: {soma}")
    print(f"A média das idades é: {media}")







lista_pessoas()