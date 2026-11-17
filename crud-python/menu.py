from estado import Estado


def _ler_id():
    try:
        valor = int(input("ID do estado: "))
        if valor < 1:
            raise ValueError
        return valor
    except ValueError:
        print("Informe um ID inteiro positivo.")
        return None


def estado():
    while True:
        print("\n## MENU ##")
        print("1. Cadastrar Estado")
        print("2. Listar Estados")
        print("3. Atualizar Estado")
        print("4. Excluir Estado")
        print("0. Sair")
        opcao = input("=> ").strip()

        if opcao == "0":
            print("Até logo!")
            break
        if opcao == "1":
            print("\n## Cadastro de Estado ##")
            item = Estado()
            item.nome = input("Nome: ").strip()
            item.sigla = input("Sigla: ").strip().upper()
            if not item.nome or not item.sigla:
                print("Nome e sigla são obrigatórios.")
            else:
                item.salvar()
        elif opcao == "2":
            print("\n## Estados cadastrados ##")
            estados = Estado().listar()
            if estados:
                for item in estados:
                    print(f"ID: {item['id']}, Nome: {item['nome']}, Sigla: {item['sigla']}")
            else:
                print("Nenhum estado cadastrado.")
        elif opcao == "3":
            print("\n## Atualizar Estado ##")
            item = Estado()
            item.id = _ler_id()
            if item.id is not None:
                item.nome = input("Novo nome: ").strip()
                item.sigla = input("Nova sigla: ").strip().upper()
                if not item.nome or not item.sigla:
                    print("Nome e sigla são obrigatórios.")
                else:
                    item.atualizar()
        elif opcao == "4":
            print("\n## Excluir Estado ##")
            item = Estado()
            item.id = _ler_id()
            if item.id is not None:
                item.excluir()
        else:
            print("Opção inválida.")
