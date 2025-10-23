def mostrar_estatisticas(pacientes):    
    if not pacientes:
        print("Nenhum paciente cadastrado para calcular estatísticas.")
        return

    total_pacientes = len(pacientes)
    soma_idades = sum(paciente["idade"] for paciente in pacientes)
    idade_media = soma_idades / total_pacientes

    paciente_mais_novo = min(pacientes, key=lambda p: p["idade"])
    paciente_mais_velho = max(pacientes, key=lambda p: p["idade"])

    print("\n=== Estatísticas dos Pacientes ===")
    print(f"Total de pacientes cadastrados: {total_pacientes}")
    print(f"Idade média dos pacientes: {idade_media:.2f} anos")
    print(f"Mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")