velocidade = float(input("Qual a velocidade do carro?" ))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print("Velocidade dentro do intervalo permitido.")

else:
    print("Você foi multado por ultrapassar o limite de velocidade permitido!")
    print(f'Valor da multa é R${multa}')
    