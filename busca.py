def buscar_paciente(pacientes):
    cpf_busca = input("Digite o CPF do paciente que deseja buscar: ").strip()
    
    paciente_encontrado = None
    for paciente in pacientes:
        if paciente["cpf"] == cpf_busca:
            paciente_encontrado = paciente
            break
    
    if paciente_encontrado:
        print("Paciente encontrado:")
        print(f"Nome: {paciente_encontrado['nome']}")
        print(f"Idade: {paciente_encontrado['idade']}")
        print(f"Telefone: {paciente_encontrado['telefone']}")
        print(f"CPF: {paciente_encontrado['cpf']}")
    else:
        print("Paciente não encontrado.")