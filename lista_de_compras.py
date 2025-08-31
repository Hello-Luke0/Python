def main():

    def adionarProduto():
        print("Qual produto você deseja?")
        produto = input()
        quantidade = int(input("Digite a quantidade desejada: "))

        while quantidade <= 0:  # Repete enquanto a quantidade for 0 ou menor
            print("\nQuantidade inválida!")
            quantidade = int(input("Digite a quantidade desejada: "))

        produtos_dentro_da_lista.append(produto)  # adiona o produto na lista
        qtd_produtos_na_lista.append(quantidade)  # adiona a quantidade do produto na lista

        print("\nProduto adionado com sucesso")

    def removerProduto():
        print("Qual produto deseja remover?")
        produto = input()

        if produto in produtos_dentro_da_lista:  # verifica se o produto está dentro da lista

            del qtd_produtos_na_lista[produtos_dentro_da_lista.index(produto)]  # remove o valor pelo índice da lista
            produtos_dentro_da_lista.remove(produto)  # remove o valor a partir do nome que está dentro do índice
            print("Produto removido!")

        else:
            print("Produto não encontrado!")

    def procurarProduto():
        if produtos_dentro_da_lista:  # Verifica se há algo na sua lista primeiramente

            print("\nProdutos na sua lista:")
            for item in produtos_dentro_da_lista:
                print("--> " + item)

            print("\nQual produto deseja pesquisar?")
            produto = input()

            if produto in produtos_dentro_da_lista:
                print("\nEste produto está na lista")
                print("Você tem essa quantidade: ", qtd_produtos_na_lista[produtos_dentro_da_lista.index(produto)])
            else:
                print("\nEste produto não está na lista")

        else:
            print("\nNão há nada na sua lista no momento.")

    def fecharSistema():
        print("Obrigado! Volte sempre.")

    produtos_dentro_da_lista = []
    qtd_produtos_na_lista = []

    print("\nBem Vindo!")

    while True:
        #Faixa de opções
        print("O que você deseja?\n")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Pesquisar produto")
        print("4 - Sair")

        option = input("\nDigite a opção desejada: ")
        if option.isnumeric():

            if int(option) == 1:
                adionarProduto()

            elif int(option) == 2:
                removerProduto()

            elif int(option) == 3:
                procurarProduto()

            elif int(option) == 4:
                fecharSistema()
                break

            else:
                print("Opção inválida! Escolha uma das opções na tela\n")

        else:
            print("Opção inválida! Escolha uma das opções na tela\n")
            continue

main()
