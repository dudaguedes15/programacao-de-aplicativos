idade = int(input("Digite a sua idade: "))
dinheiro = float(input("Digite o saldo que tem em sua carteira: "))

if idade >= 18 and dinheiro >= 50: 
    print("Acesso autorizado! Bem vindo ao evento!")

elif idade < 18 and dinheiro < 50: 
    print("Infelizmente você não cumpre os requisitos  de entrada.")

elif idade >= 18 and dinheiro < 50:
    print("Infelizmento você não cumpre os requisitos de entrada.")

elif idade < 18 and dinheiro >= 50:
    print("Infelizmente você não cumpre os requisitos de entrada.")