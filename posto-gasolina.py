from enum import Enum


class Combustivel (Enum):
    GASOLINA = 1
    ALCOOL = 2

def bomba_combustivel():
    preco_inteiro = 0
    valor_gasolina = 5.90
    valor_alcool = 4.50
    print("Você quer qual combustível?")
    escolha = int(input())
    if escolha == Combustivel.GASOLINA.value:
        print("Quantos litros de combustivel?")
        qtdCombustivel = int(input())
        preco_inteiro = qtdCombustivel * valor_gasolina
        if qtdCombustivel <= 20:
            precoFinal = 0
            precoFinal = preco_inteiro - (preco_inteiro * 0.04)
        else:
            precoFinal = preco_inteiro - (preco_inteiro * 0.06)
        print(f"O valor será: R${precoFinal}")
    elif escolha == Combustivel.ALCOOL.value:
        print("Quantos litros de combustivel?")
        qtdCombustivel = int(input())
        preco_inteiro = qtdCombustivel * valor_alcool
        if qtdCombustivel <= 20:
            precoFinal = 0
            precoFinal = preco_inteiro - (preco_inteiro * 0.03)
        else:
            precoFinal = preco_inteiro - (preco_inteiro * 0.05)
        print(f"O valor será: R${precoFinal}")
    else:
        print("Opção inexistente") 
        bomba_combustivel()  



bomba_combustivel()