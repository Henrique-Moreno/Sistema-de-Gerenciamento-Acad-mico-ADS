# =======================================
# Sistema de Gerenciamento Acadêmico
# Nome: [ Henrique Alexandre ]
# Curso: [Tecnologia em Análise e Desenvolvimento de Sistemas]
# =======================================

import json

# Caminhos para os arquivos de dados
ARQUIVOS = {
    "estudantes": "estudantes.json",
    "professores": "professores.json",
    "disciplinas": "disciplinas.json",
    "turmas": "turmas.json",
    "matriculas": "matriculas.json"
}

# Função para carregar dados de um arquivo JSON
def carregar_dados(modulo):
    try:
        with open(ARQUIVOS[modulo], 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Erro ao carregar os dados de {modulo}.")
        return []

# Função para salvar dados em um arquivo JSON
def salvar_dados(modulo, dados):
    with open(ARQUIVOS[modulo], 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função para incluir registros
def incluir_registro(modulo, dados_necessarios):
    print(f"===== INCLUSÃO ({modulo.upper()}) =====")
    registro = {}
    for campo, tipo in dados_necessarios.items():
        while True:
            valor = input(f"{campo}: ")
            try:
                registro[campo] = tipo(valor)
                break
            except ValueError:
                print(f"Valor inválido para {campo}. Tente novamente.")
    registros = carregar_dados(modulo)
    registros.append(registro)
    salvar_dados(modulo, registros)
    print(f"{modulo.capitalize()} adicionado com sucesso!")

# Função para listar registros
def listar_registros(modulo):
    print(f"===== LISTAGEM ({modulo.upper()}) =====")
    registros = carregar_dados(modulo)
    if not registros:
        print(f"Não há {modulo} cadastrados.")
    else:
        for registro in registros:
            print(registro)
    input("Pressione ENTER para continuar.")

# Função para atualizar registros
def atualizar_registro(modulo, campo_chave):
    print(f"===== ATUALIZAÇÃO ({modulo.upper()}) =====")
    registros = carregar_dados(modulo)
    chave = input(f"Informe o {campo_chave} do registro a ser atualizado: ")
    for registro in registros:
        if str(registro[campo_chave]) == chave:
            print("Registro atual:")
            print(registro)
            for campo in registro:
                novo_valor = input(f"{campo} (Atual: {registro[campo]}): ")
                if novo_valor:
                    registro[campo] = novo_valor
            salvar_dados(modulo, registros)
            print("Registro atualizado com sucesso!")
            return
    print("Registro não encontrado.")

# Função para excluir registros
def excluir_registro(modulo, campo_chave):
    print(f"===== EXCLUSÃO ({modulo.upper()}) =====")
    registros = carregar_dados(modulo)
    chave = input(f"Informe o {campo_chave} do registro a ser excluído: ")
    for registro in registros:
        if str(registro[campo_chave]) == chave:
            registros.remove(registro)
            salvar_dados(modulo, registros)
            print("Registro excluído com sucesso!")
            return
    print("Registro não encontrado.")

# Função para exibir o menu de operações de um modulo
def menu_operacoes(modulo, dados_necessarios, campo_chave):
    while True:
        print(f"***** MENU DE OPERAÇÕES ({modulo.upper()}) *****")
        print("(1) Incluir.")
        print("(2) Listar.")
        print("(3) Atualizar.")
        print("(4) Excluir.")
        print("(9) Voltar ao menu principal.")
        print("******************************************")
        opcao = input("Informe a ação desejada: ")

        if opcao == "1":
            incluir_registro(modulo, dados_necessarios)
        elif opcao == "2":
            listar_registros(modulo)
        elif opcao == "3":
            atualizar_registro(modulo, campo_chave)
        elif opcao == "4":
            excluir_registro(modulo, campo_chave)
        elif opcao == "9":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função principal
def sistema():
    dados_sistema = {
        "estudantes": {"nome": str},
        "professores": {"codigo": int, "nome": str, "cpf": str},
        "disciplinas": {"codigo": int, "nome": str},
        "turmas": {"codigo": int, "codigo_professor": int, "codigo_disciplina": int},
        "matriculas": {"codigo_turma": int, "codigo_estudante": int}
    }
    campo_chave = {"estudantes": "nome", "professores": "codigo", "disciplinas": "codigo", "turmas": "codigo", "matriculas": "codigo_turma"}

    while True:
        print("***** MENU PRINCIPAL *****")
        print("(1) Estudantes")
        print("(2) Professores")
        print("(3) Disciplinas")
        print("(4) Turmas")
        print("(5) Matrículas")
        print("(9) Sair")
        print("***************************")
        opcao = input("Informe a ação desejada: ")

        if opcao in "12345":
            modulo = list(dados_sistema.keys())[int(opcao) - 1]
            menu_operacoes(modulo, dados_sistema[modulo], campo_chave[modulo])
        elif opcao == "9":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o sistema
if __name__ == "__main__":
    sistema()
