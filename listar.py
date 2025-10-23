def listar_pacientes(pacientes):
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    print("\nLista de Pacientes Cadastrados:")
    for idx, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente {idx}:")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"Telefone: {paciente['telefone']}")
        print(f"CPF: {paciente['cpf']}")