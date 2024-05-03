def calculadora_imc():
    peso = 0
    altura = 0
    print("digite o seu peso")
    peso = int(input())
    print("digite sua altura")
    altura = float(input())

    imc = peso / (altura * altura)

    if imc < 20:
        print("Abaixo do peso")
    elif imc >= 20 and imc <= 25:
        print("Peso normal")
    elif imc > 25 and imc <=30:
        print("Sobrepeso")
    elif imc < 30 and imc >= 40:
                print("Obesidade")
    elif imc > 40:
        print("Obesidade grave")
    else:
        print("Erro")




calculadora_imc()