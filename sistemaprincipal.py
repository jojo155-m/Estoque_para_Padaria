from sys import exit
import json
from os import system

banco_de_dados = 'bancodedados.json'
estoque = {}
vendas = []

try:
    with open(banco_de_dados, 'r', encoding='utf8') as estoquedosistema:
        dados = json.load(estoquedosistema)
        estoque = dados.get("estoque", {})
        vendas = dados.get("vendas", [])
except FileNotFoundError:
    with open(banco_de_dados, 'w') as estoquedosistema:
        json.dump({"estoque": estoque, "vendas": vendas}, estoquedosistema)

def titulo(msg):
    print("=-" * 15)
    print(f"{msg:^30}")
    print("=-" * 15)

def erro(con):
    print(f"{con} Erro: opção não encontrada")

def func_verifica_numero(num, tipo):
    tester, verify = isnumber(num, tipo)
    if verify:
        while tester:
            num = input("ERROR! Digite um número válido: ").replace(",", ".")
            tester, verify = isnumber(num, tipo)
        return tipo(num)
    else:
        return tipo(num)

def isnumber(num, tipo):
    try:
        tipo(num)
        return False, False
    except ValueError:
        return True, True

def cadastrar_produto():
    system("cls")
    titulo("CADASTRAR PRODUTO")
    nome = input("Nome do produto: ").capitalize()
    tipo = input("Tipo do produto: ")
    valor = func_verifica_numero(input("Preço de venda: ").replace(",", "."), float)
    estoque_inicial = func_verifica_numero(input("Quantos itens em estoque?: "), int)

    if nome and tipo and valor and estoque_inicial:
        identificador = len(estoque) + 1
        estoque[identificador] = {
            "nome": nome,
            "tipo": tipo,
            "valor": valor,
            "quantidade": estoque_inicial
        }
        print("Cadastro realizado com sucesso!")
    else:
        print("Campos obrigatórios não preenchidos.")

def realizar_venda():
    system("cls")
    titulo("REALIZAR VENDA")
    nome = input("Digite o nome do produto a ser vendido: ")

    for identificador, produto in estoque.items():
        if produto['nome'].lower() == nome.lower():
            quantidade = func_verifica_numero(input(f"Quantidade desejada ({produto['quantidade']} em estoque): "), int)

            if quantidade <= produto['quantidade']:
                produto['quantidade'] -= quantidade
                valor_total = produto['valor'] * quantidade
                venda = {
                    "identificador_produto": identificador,
                    "nome_produto": produto['nome'],
                    "quantidade_vendida": quantidade,
                    "valor_total": valor_total
                }
                vendas.append(venda)
                print(f"Venda de {nome} realizada com sucesso! Valor total: R${valor_total:.2f}")
            else:
                print("Quantidade insuficiente em estoque.")
            return
    else:
        print("Produto não encontrado.")

def alterar_produto():
    system("cls")
    titulo("ALTERAR PRODUTO")
    nome = input("Digite o nome do produto a ser alterado: ")

    for identificador, produto in estoque.items():
        if produto['nome'].lower() == nome.lower():
            novo_nome = input(f"Novo nome ({produto['nome']}): ").capitalize()
            novo_tipo = input(f"Novo tipo ({produto['tipo']}): ")
            novo_valor = func_verifica_numero(input(f"Novo preço de venda ({produto['valor']}): ").replace(",", "."), float)
            novo_estoque = func_verifica_numero(input(f"Novo estoque ({produto['quantidade']}): "), int)

            if novo_nome:
                produto['nome'] = novo_nome
            if novo_tipo:
                produto['tipo'] = novo_tipo
            if novo_valor:
                produto['valor'] = novo_valor
            if novo_estoque:
                produto['quantidade'] = novo_estoque

            print("Alteração realizada com sucesso!")
            return
    else:
        print("Produto não encontrado.")

def relatorio_produtos():
    system("cls")
    titulo("RELATÓRIO DE PRODUTOS")
    print("1 - Relatório de todos os produtos.")
    print("2 - Relatório de vendas realizadas.")

    opcao = input("Digite o número da opção desejada: ")
    opcao = func_verifica_numero(opcao, int)

    match opcao:
        case 1:
            print("{:<10} {:<20} {:<15} {:<10} {:<10}".format("Identificador", "Nome", "Tipo", "Preço", "Quantidade"))
            for identificador, produto in estoque.items():
                print("{:<14} {:<20} {:<15} R${:<9.2f} {:<10}".format(
                    identificador, produto['nome'], produto['tipo'], produto['valor'], produto['quantidade']))
        case 2:
            print("{:<10} {:<20} {:<10} {:<15}".format("Identificador", "Nome", "Quantidade", "Valor Total"))
            for venda in vendas:
                print("{:<14} {:<20} {:<10} R${:<9.2f}".format(
                    venda['identificador_produto'], venda['nome_produto'],
                    venda['quantidade_vendida'], venda['valor_total']))
        case _:
            erro("Opção")

while True:
    titulo("MENU PRINCIPAL")
    print("1 - Cadastrar Produto")
    print("2 - Alterar Produto")
    print("3 - Realizar Venda")
    print("4 - Relatório de Produtos")
    print("5 - Sair")

    opcao = input("Digite o número da opção desejada: ")
    opcao = func_verifica_numero(opcao, int)

    match opcao:
        case 1:
            cadastrar_produto()
        case 2:
            alterar_produto()
        case 3:
            realizar_venda()
        case 4:
            relatorio_produtos()
        case 5:
            break
        case _:
            erro("Opção")

with open(banco_de_dados, 'w') as arquivo:
    json.dump({"estoque": estoque, "vendas": vendas}, arquivo, indent=2)
