compras = []

def adicionar():
    print('Adicionar Produto')
    produto = input('Nome do produto: ')
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: R$'))
    item = (produto, quantidade, preco)
    compras.append(item)


def imprimir():
    print('Lista de Compras')
    total = num_item = 0

    for item in compras:
        num_item += 1
        print(f'{num_item} - {item[0]}, {item[1]} x R${item[2]:.2f} = R${(item[1] * item[2]):.2f}')
        total += item[1] * item[2]

    print(f'Total: R${total:.2f}')

def remover():
    print('Remover Produto')
    imprimir()
    remove = int(input('Qual o número do produto que quer remover? '))
    compras.pop(remove - 1)

def main():
    while True:
        print('''
===========================
1 - Adicionar Protudo
2 - Remover Produto
3 - Imprimir Lista 
4 - Sair 
===========================
    ''')
        opcao = ' '
        while opcao not in '1234':
            opcao = input('Opção: ')

        if opcao == '1':
            adicionar()
        elif opcao == '2':
            remover()
        elif opcao == '3':
            imprimir()
        elif opcao == '4':
            imprimir()
            print('Fim do Programa')
            break

main()
