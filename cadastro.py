def cadastrar_paciente(pacientes):
    nome = input("Digite o nome do paciente: ")
    while True:
        try:
            idade = int(input("Digite a idade do paciente: "))
            telefone = int(input("Digite o telefone do paciente: "))
            cpf = int(input("Digite o CPF do paciente: "))
            break
        except ValueError:
            print("Dado inválido. Por favor, insira um número inteiro, sem pontos.")
    
    
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "cpf": cpf
    }
    pacientes.append(paciente)
    print("\nPaciente cadastrado com sucesso!")
