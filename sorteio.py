ide = int(input("Qual o seu ID?: "))
compra = float(input("Qual o valor da compra?: "))

if ide % 2 == 0 and compra > 500.0:
    print(f"Parabéns, usuário {ide}! Você ganhou um cupom para sua compra de R$: {compra}.")
else:
    print(f"Obrigado pela compra, usuário {ide}. Continue acompanhando nossas promoções!")