print("*******************************************")
print("*                                         *")
print("*            Programa Saudavel            *")
print("*                                         *")
print("*******************************************")
print("(Visamos o bem-estar do usuário)")

user = input("Digite seu nome: ")
print("")
print(f"Olá {user}!")
while True:
    try:
        altura = float(input("Qual a sua altura? (Digite cada parametro usando o '.' para casas decimais nos números.) "))
        break
    except ValueError:
        print("\nDigite um valor válido.")

while True:
    try:
        peso = float(input("\nQual o seu peso? "))
        break
    except ValueError:
        print("\nDigite um valor válido.")


imc = peso / (altura * altura)

if imc < 18.5:
    print(f"\nSeu IMC e {imc:.2f}")
    imc = print("Magreza")
    orientacao = "Você precisa se alimentar melhor."
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC e {imc:.2f}")
    imc = print("Normal")
    orientacao = "Você está no peso ideal!"
elif imc >= 25 and imc < 30:
    print(f"Seu IMC e {imc:.2f}")
    imc = print("Sobrepeso")
    orientacao = "Você aparenta estar bem, porém um pouco acima do peso."
elif imc >= 30 and imc < 40:
    print(f"Seu IMC e {imc:.2f}")
    imc = print("Obesidade")
    orientacao = "Você está com obesidade. Siga as orientações das dicas abaixo e busque ajuda do seu médico."	
else:
    print(f"Seu IMC e {imc:.2f}")
    imc = print("Obesidade grave")

print(orientacao)
print("")
while True:
    try:
        perg1 = int(input("\nVocê se exercita regularmente? (Digite '1' para 'sim' ou '2' para 'não'): "))
        if perg1 in [1, 2]:
            break
        else:
            print("\nPor favor, digite '1' para 'sim' ou '2' para 'não'.")
    except ValueError:
        print("\nPor favor, digite '1' para 'sim' ou '2' para 'não'.")

if perg1 == 1:
    print("Parabéns! Continue assim.")
else:
    print("Procure se exercitar mais.")