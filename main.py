from cadastro import cadastrar_paciente
from estatisticas import mostrar_estatisticas
from busca import buscar_paciente
from listar import listar_pacientes

pacientes = []

while True:
    print("\n === Sistema Clínica Vida+ ===")
    print("1 - Cadastrar Paciente")
    print("2 - Ver estatísticas")
    print("3 - Buscar Paciente")
    print("4 - Listar todos os Pacientes")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_paciente(pacientes)
    elif opcao == "2":
        mostrar_estatisticas(pacientes)
    elif opcao == "3":
        buscar_paciente(pacientes)
    elif opcao == "4":
        listar_pacientes(pacientes)
    elif opcao == "5":
        print("Encerrando o sistema... Até logo!")
        break
    else:
        print("Opção inválida")