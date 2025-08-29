import os
escolha = [1, 2, 3]
continuar = 's'
cont = 's'
temp = []
lista_usuario = []
lista_usuario2 = []
lista_cod = []
lista_prod = []
temp_cod = []
lista_prof = []
lista_produtos = []
cod_ind = []
perfil = 0
valor_lista = None
lista_prod_adc = []

def menu():
    print('\nMenu Principal do Sistema')
    print('\n1 - Administrador')
    print('\n2- Operador')
    print('\n0 - Sair')
    opçao = input("Escolha uma das opções:\n")
    while (opçao == "" or (opçao != "0" and opçao != "1" and opçao != "2")):
        print("Escolha uma opção válida!!")
        opçao = input("Escolha uma das opções válidas:\n")
    return opçao

def admin():
    print('\n1 - Cadastrar')
    print('\n2 - Listar')
    print('\n3 - Editar')
    print('\n4 - Excluir')
    print('\n0 - Voltar ao menu principal')
    esco = input('Digite a opção desejada:\n')
    while (esco == "" or (esco != "0" and esco != "1" and esco != "2" and esco != "3" and esco != "4")):
        print('Escolha uma opção válida.')
        esco = input('Digite a opção desejada:\n')
    return esco

def cadastrar():
    print("Rotina para cadastrar produtos\n")
    cont_cad = 1
    while cont_cad != 2:
        arquivo = open('comidas.txt', 'a+', encoding='utf-8')
        cod = busca_cod()
        print("Código do produto a ser cadastrado: %s" %(cod))
        desc = input("Insira a descrição do produto a ser cadastrado\n")
        while desc == "":
            print("Insira uma descrição válida")
            desc = input('Digite o produto que deseja inserir para o código %s\n' %(cod))
        valor = input('Digite o valor que deseja para o(a) %s\n' %(desc))
        while (valor == "" or valor.isalpha()):
            print("Insira um valor válido\n")  
            valor = float (input('Digite o valor que deseja para o(a) %s\n' %(desc)))
        conf_cad = input('Deseja confirmar o cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n\n')
        while (conf_cad != "1" and conf_cad != "2"):
            print("Insira uma opção válida\n")
            conf_cad = input('Deseja confirmar o cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n\n')
        if conf_cad == "1":
            arquivo = open('comidas.txt', 'r', encoding='utf-8')
            dados = arquivo.readlines()
            arquivo.close()
            arquivo = open('comidas.txt', 'a+', encoding='utf-8')
            if dados == []:
                arquivo.write(str(cod) + ';' + desc + ';' + valor + '\n')
                arquivo.close()
            else:
                for i in range(len(dados)):
                    dados[i] = dados[i].strip('\n').split(';')
                dados.append([cod, desc, valor]) 
                lista_cad = sorted(dados, key=lambda x: int(x[0]))  
                arquivo = open('comidas.txt', 'w', encoding='utf-8')
                for i in range(len(lista_cad)):
                    arquivo.write(str(lista_cad[i][0]) + ";" + str(lista_cad[i][1]) + ";" + str(lista_cad[i][2]) + "\n")
                arquivo.close()   
            print("Item cadastrado com sucesso!!\n\n")   
            cont_cad = 2          
        elif conf_cad == "2":
            print("Cadastro cancelado\n")
            cont_cad = 2

def busca_cod():
    codigo = 0
    arquivo = open('comidas.txt', 'r', encoding='utf-8')
    dados = arquivo.readlines()
    if dados == []:
        codigo = 100
    else:
        for i in range(len(dados)):
            dados[i] = dados[i].strip('\n')
            dados[i] = dados[i].split(';')
            temp.append(dados[i][0])
            arquivo.close()
 
        for i in range(len(temp)):
            temp[i] = int(temp[i])  
        numeros = set(temp)
        esperado = set(range(100, max(numeros) + 1))
        faltantes = sorted(esperado - set(numeros))
        if faltantes == []:
            codigo = str(max(temp) + 1)
        else:
            for numero in faltantes:
                temp_cod.append(numero)
            codigo = str(temp_cod[0])
    return codigo

def listar():
    print("\nListagem de produtos disponíveis\n")
    arquivo_list = open('comidas.txt', 'r', encoding='utf-8')
    dados_list = arquivo_list.readlines()
    lista_prod.clear()
    if dados_list == []:
        print("\nNão há produtos disponíveis\n")
    else:
        print("Código - Descrição - Valor Unitário")
        for i in range(len(dados_list)):
            dados_list[i] = dados_list[i].strip("\n")
            dados_list[i] = dados_list[i].split(";")
            lista_prod.append(dados_list[i])
        for j in range(len(lista_prod)):
            print(lista_prod[j][0] + " - " + lista_prod[j][1] + " - " + " R$ " + lista_prod[j][2])

def buscar_ind():
    for i in range(len(lista_prod)):
        cod_ind.append(lista_prod[i][0])
    opp = input("Escolha o código do produto desejado\n")
    while op not in cod_ind:
        listar()
        opp = input ("Escolha um código válido\n")
    codigo = cod_ind.index(opp)
    return codigo

def grav_txt():
    arquivo = open('comidas.txt', 'w', encoding='utf-8')
    for i in range(len(lista_prod)):
        arquivo.write(lista_prod[i][0] + ';' + lista_prod[i][1] + ';' + lista_prod[i][2]+ '\n')
    arquivo.close()

def alterar():
    lista_prod.clear()
    listar()
    print("\nAlterar produtos cadastrados.\n")
    for i in range(len(lista_prod)):
        lista_cod.append(lista_prod[i][0])
    alterar_opcao = input("\nEscolha o código do produto que queira alterar\n")
    while alterar_opcao not in lista_cod:
        alterar_opcao = input("Escolha um código na lista de produtos\n")
    alterar_codigo = lista_cod.index(alterar_opcao)
    print("A descrição do produto atual é %s\n" %(lista_prod[alterar_codigo][1]))
    nova_desc = input("Insira uma nova descrição do produto\n")
    while (nova_desc == ""):
        print("Insira uma descrição válida\n")
        nova_desc = input("Insira uma nova descrição do produto\n")
    print("O valor do produto atual é %s\n" %(lista_prod[alterar_codigo][2]))
    novo_valor = input("Insira um novo valor pro produto\n")
    while (novo_valor == "" or novo_valor.isalpha()):
        print("Insira um valor válido\n")
        novo_valor = input("Insira um novo valor pro produto\n")
    print("\nA nova descrição do produto sendo o código %s é %s\n" %(lista_cod[alterar_codigo],nova_desc))
    print("\nO novo valor do produto %s é R$%s\n" %(nova_desc, novo_valor))
    lista_prod[alterar_codigo][1] = nova_desc
    lista_prod[alterar_codigo][2] = novo_valor
    archive = open('comidas.txt', 'w', encoding='utf-8')
    for i in range(len(lista_prod)):
        archive.write(lista_prod[i][0] + ";" + lista_prod[i][1] + ";" + lista_prod[i][2] + "\n")
    archive.close()

def excluir():
    lista_prod.clear()
    listar()
    print("\nAlterar produtos cadastrados.\n")
    for i in range(len(lista_prod)):
        lista_cod.append(lista_prod[i][0])
    excluir_opcao = input("\nEscolha o código do produto que queira excluir\n")
    while excluir_opcao not in lista_cod:
        excluir_opcao = input("Escolha um código na lista de produtos\n")
    excluir_codigo = lista_cod.index(excluir_opcao)
    lista_prod.pop(excluir_codigo)
    archive = open('comidas.txt', 'w', encoding='utf-8')
    for i in range(len(lista_prod)):
        archive.write(lista_prod[i][0] + ";" + lista_prod[i][1] + ";" + lista_prod[i][2] + "\n")
    archive.close()

def pedido():
    lista_prod_adc.clear()
    lista_produtos.clear()
    valor_total_geral = 0.0
    continuar_pedido = "1"
    while continuar_pedido == "1":
        listar()
        cod = input("Insira o código do produto:\n")
        while cod == "":
            print("Insira um campo de código válido.")
            cod = input("Digite um código do produto:\n")
        arquivo = open('comidas.txt', 'r', encoding='utf-8')
        conteudo = arquivo.readlines()
        arquivo.close()
        produto_encontrado = None
        for i in conteudo:
            partes = i.strip().split(";")
            if partes[0] == cod:
                produto_encontrado = partes
            lista_produtos.append(partes)
        if produto_encontrado is None:
            print("Produto não encontrado. Tente novamente.")
            continue
        print("\nCódigo - Descrição - Valor Unitário")
        print(f"{produto_encontrado[0]} - {produto_encontrado[1]} - R$ {produto_encontrado[2]}")
        qntd = input("Digite a quantidade que deseja:\n")
        while not qntd.isdigit() or int(qntd) <= 0:
            print("Insira uma quantidade válida.")
            qntd = input("Digite a quantidade que deseja:\n")
        qntd = int(qntd)
        valor_unitario = float(produto_encontrado[2])
        subtotal = qntd * valor_unitario
        confirmar = input("Deseja confirmar o pedido deste item?\nDigite 1 para Sim\nDigite 2 para Não\n")
        while confirmar != "1" and confirmar != "2":
            print("Escolha uma opção válida.")
            confirmar = input("Digite 1 para Sim\nDigite 2 para Não\n")
        if confirmar == "1":
            print("Produto adicionado ao pedido.")
            lista_prod_adc.append([produto_encontrado[0], produto_encontrado[1], produto_encontrado[2], str(qntd)])
            valor_total_geral += subtotal
        else:
            print("Item cancelado.")
        continuar_pedido = input("Deseja adicionar mais produtos?\nDigite 1 para Sim\nDigite 2 para Finalizar o pedido\n")
        while continuar_pedido != "1" and continuar_pedido != "2":
            print("Escolha uma opção válida.")
            continuar_pedido = input("Digite 1 para Sim\nDigite 2 para Finalizar o pedido\n")
    if len(lista_prod_adc) > 0:
        print("\n=== Resumo do Pedido ===")
        print("Código - Produto - Valor Unitário - Quantidade - Subtotal")
        for item in lista_prod_adc:
            cod = item[0]
            nome = item[1]
            valor = float(item[2])
            quantidade = int(item[3])
            subtotal = valor * quantidade
            print(f"{cod} - {nome} - R$ {valor:.2f} - {quantidade}x - R$ {subtotal:.2f}")
        print(f"\nTOTAL A PAGAR: R$ {valor_total_geral:.2f}")
        print("Pedido finalizado com sucesso!\n")
    else:
        print("Nenhum produto foi adicionado ao pedido.\n")

while continuar == 's':
    perfil = menu()
    if perfil == '0':
        continuar = 'n'
    elif perfil == '1':
        cont = 's'
        while cont == 's':
            op = admin()
            if op == '0':
                cont = 'n'
            elif op == "1":
                cadastrar()
            elif op == "2":
                listar()
            elif op == "3":
                alterar()
            elif op == "4":
                excluir()
    else:
        pedido()