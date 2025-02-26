print("*******************************************")
print("*                                         *")
print("*            Programa Saudável            *")
print("*                                         *")
print("*******************************************")
print("(Visamos o bem-estar do usuário)")

pacientes = []  
dados_pacientes = []  

while True:
    usuario = input("\nDigite seu nome (ou 'sair' para encerrar): ")
    if usuario.lower() == "sair":
        break
    else:
        altura = float(input("\nQual a sua altura? (Use '.' para casas decimais): "))
        peso = float(input("\nQual o seu peso?: "))
        
        imc = peso / (altura ** 2)
        
        pacientes.append(usuario)
        dados_pacientes.append((altura, peso, imc))
        
        print(f"\n{usuario}, seu IMC é {imc:.2f}")
        
        if imc < 18.5:
            print("Você está em estado de magreza. É importante se alimentar melhor.")
        elif 18.5 <= imc < 25:
            print("Você está no peso ideal, continue assim!")
        elif 25 <= imc < 30:
            print("Você está um pouco acima do peso. Considere adotar hábitos saudáveis.")
        elif 30 <= imc < 40:
            print("Você está com obesidade. Siga orientações médicas e adote um estilo de vida mais saudável.")
        else:
            print("Obesidade grave. Busque ajuda médica urgentemente.")

print("\nResumo dos Pacientes Cadastrados:")
if len(pacientes) != 0:
    for i, paciente in enumerate(pacientes):
        altura, peso, imc = dados_pacientes[i]
        print(f"{paciente} - Altura: {altura:.2f}m, Peso: {peso:.2f}kg, IMC: {imc:.2f}")
else:
    print("\nNenhum paciente foi atendido")
print("\nTenha um ótimo dia!")

# Nomes dos membros da equipe que contribuiu com o trabalho abaixo:
membro1 = "Reginaldo Ytalo Félix Mota"
membro2 = "Paulo André Santos Queiroz"
membro3 = "João Luis"

print(f"\nMade by: {membro1}, {membro2} e {membro3}. \n All Rights Reserved - 2025")