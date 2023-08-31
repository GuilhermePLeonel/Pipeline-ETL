import json

characters = json.loads(open("meu_desafio_pipeline/naruto.json").read())["characters"]


# EXTRAÇÃO
def get_all_characters():
    for character in characters:
        print("\n")
        for key, value in character.items():
            print(f"""    {key}: {value}""")


def get_character_by_name(nome):
    for character in characters:
        print("\n")
        if nome.lower() in character["nome"].lower():
            print(
                """    Aqui estão as informações do personagem que você pesquisou:\n"""
            )
            for key, value in character.items():
                print(f"""    {key}: {value}""")
            break
    else:
        print("\n    ***Personagem não encontrado!***")


def get_characters_by_id(id):
    for character in characters:
        if character["id"] == id:
            for key, value in character.items():
                print(f"""    {key}: {value}""")


# LOAD
def add_character(nome, idade, aldeia, sensei, rank):
    id = len(characters) + 1
    character = {
        "id": id,
        "nome": nome,
        "idade": idade,
        "aldeia": aldeia,
        "sensei": sensei,
        "rank": rank,
    }
    characters.append(character)
    with open("meu_desafio_pipeline/naruto.json", "w") as file:
        json.dump({"characters": characters}, file, indent=4)


def edit_character(nome, campo, novo_valor):
    for character in characters:
        if nome.lower() in character["nome"].lower():
            character[campo] = novo_valor
            with open("meu_desafio_pipeline/naruto.json", "w") as file:
                json.dump({"characters": characters}, file, indent=4)
            print("\n    Personagem editado com sucesso!")
            break
    else:
        print("\n    ***Personagem não encontrado!***")


# TRANSFORMAÇÃO
def main():
    print(
        f"""\n
    ========== Seja bem vindo ao Bnaco de Dados Naruto ==========
    
    [1] - Listar todos os personagens
    [2] - Pesquisar personagem por nome
    [3] - Pesquisar personagem por id  
    [4] - Adcionar personagem
    [5] - Editar personagem
    [6] - Sair
    """
    )
    opção = input(
        """
    Escolha uma das opções cima: """
    )
    match opção:
        case "1":
            print("""\n   Aqui está a lista de todos os personagens:""")
            get_all_characters()
        case "2":
            nome = input("""\n    Digite o nome do personagem que quer pesquisar: """)
            get_character_by_name(nome)
        case "3":
            id = int(input("""\n    Digite o ID do personagem que quer pesquisar: """))
            get_characters_by_id(id)
        case "4":
            nome = input("""\n    Digite o nome do personagem que deserja criar: """)
            idade = int(input("""\n    Digite a idade do personagem: """))
            aldeia = input("""\n    Digite o nome da vila do personagem: """)
            sensei = input("""\n    Digite o nome do sensei do personagem: """)
            rank = input("""\n    Digite o rank do personagem: """)
            add_character(nome, idade, aldeia, sensei, rank)
            print("\n    Personagem criado com sucesso!")
        case "5":
            nome = input("""\n    Digite o nome do personagem que deseja editar: """)
            campo = input(
                """\n    Escolha dentre um desses campos qual irá querer mudar [nome, idade, aldeia, sensei, rank]: """
            )
            novo_valor = input("""\n    Digite o novo valor: """)
            edit_character(nome, campo, novo_valor)
        case "6":
            print("\n    Até mais!")
        case _:
            print("\n    Opção inválida!")


main()
