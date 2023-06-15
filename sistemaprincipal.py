from sys import exit   # Importe do exit da bliblioteca sys                                                     
import json            # impote do json                                                   
from os import system  # Importe do system da bliblioteca os                                                     

banco_de_dados = 'banco.json'   # Aqui criei o Baco de dados onde sera salvo as informações cadastradas.
estoque = {}                    # Aqui criei um dicionario que armazenara os itens do estoque 

try:
    with open(banco_de_dados,'r',encoding='utf8') as estoquedosistema:
        estoque = json.load(estoquedosistema)
except FileNotFoundError:
    with open(banco_de_dados,'w') as estoquedosistema:
        json.dump(estoque,banco_de_dados)

def titulo(msg):        # Aqui criamos uma definição para criar uma interaface basica para o usuario.
    print("=-"*15)
    print(f"{msg:^15}")
    print("=-"*15)

def erro(con):
    print(f"{con} Erro:option not found")

def func_verifica_numero(num,tipo):            #Função para ver se é um input valído.
    tester,verify = isnumber(num,tipo)  
    if verify:
        while tester:
            num = ("ERROR!, Digite um número valído!! : ").replace(",",".") #Laço ocorre até obter valor valido. 
            tester,verify = isnumber(num,tipo)
        return tipo(num)
    else:
        return tipo(num)
def isnumber(num,tipo):
    try:
        tipo(num)
        return False, False 
    except ValueError:
        return True, True 

while True:
    titulo("Estoque")
    print("Estoque[1]")
    print("Alterar Estoque[2]")
    print("Sair")
    opcao = input("Digite o número da opção desejada: ")
    opcaotester = func_verifica_numero(opcao,int)
    match opcaotester:
        case 1:
            if len(estoque) == 0:
                system("cls")
                print("Estoque Vazio!")
            else:
                system("cls")
                titulo("ESTOQUE")
                print("Produtos[1]")
                print("Gerar Relatório[2]")
                opcao = input("Digite o número da opção desejada: ")
                opcaotester = func_verifica_numero(opcao,int)
            match opcaotester:
                case 1:
                    for produtos in estoque.key():
                        system("cls")
                        print(produtos)
                case 2:
                    while True:
                        system("cls")
                        print("Valor do Estoque[1]")
                        print("Quantidade Total do Estoque[2]")
                        print("Informações avançadas estoque[3]")
                        print("Voltar")
                        opcao = input("Digite o número da opção desejada: ")
                        opcaotester = func_verifica_numero(opcao,int)