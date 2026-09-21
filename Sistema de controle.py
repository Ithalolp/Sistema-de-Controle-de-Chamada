#variaveis
total_chamados = 0
problema_alto = 0
problema_medio = 0
problema_baixo = 0

#opcoes
opcoes = 0

while True:
    print("\nSuporte tecnico")
    print("1 para registrar chamado")
    print("2 para consultar seu resumo")
    print("3 para encerrar o sistema")

    #escolha de serviço
    opcao = int(input("digite a opção: 1, 2 ou 3: "))

    #registro de chamada
    if opcao == 1:
        nome = input("\nnome do funcionário? ")

        print("\ntipo de problema")
        print("1 para computador")
        print("2 para a internet")
        print("3 problema no sistema")
        print("4 problema na impressora")

        tipo = int(input("digite o numero do problema: "))

        if tipo == 1:
            problema = "computador"
        elif tipo == 2:
            problema = "internet"
        elif tipo == 3:
            problema = "Sistema"
        elif tipo == 4:
            problema = "impressora"
        else:
            problema = "outro"

        # descrição
        descricao = input("\nDescreva seu problema: ")

        print("\nGrau do problema?")
        print("1- Impede completamente o trabalho")
        print("2- Prejudica, mas nao impede")
        print("3- não interfere")

        # grau do problema
        Grau = int(input("\nEscolha o nivel 1, 2 ou 3: "))

        if Grau == 1:
            prioridade = "alto"
            problema_alto = problema_alto + 1
        elif Grau == 2:
            prioridade = "medio"
            problema_medio = problema_medio + 1
        else:
            prioridade = "baixo"
            problema_baixo = problema_baixo + 1

        # acumuladores
        total_chamados = total_chamados + 1

        # Registro
        print("funcionario:", nome)
        print("problema:", problema)
        print("prioridade:", prioridade)

    elif opcao == 2:
        print("\nquantidade de chamados registrados:", total_chamados)
        print("chamadas de alta prioridade:", problema_alto)
        print("chamadas de media prioridade:", problema_medio)
        print("chamadas de baixa prioridade:", problema_baixo)

    elif opcao == 3:
        print("encerrando o sistema")
        break

    else:
        print("opção invalida, tente novamente.")
        
        
    
    
