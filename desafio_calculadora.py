def calculadora():
    while True:
        print("---> Calculadora simples <---")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("s - Sair")

        option = (input())

        if option == "s" or option == "S":
            print("\nObrigado por utilizar a calculadora simples, até mais.")
            break

        if option not in ['1', '2', '3', '4']:
            print()
            print("Selecione uma opção válida!")
            print()
            continue

        first_number = float(input("Digite o primeiro número: "))
        second_number = float(input("Digite os segundo número: "))

        if(option == '1'):
            result = first_number + second_number
            print("O valor da soma é: ", result)
            print()

        if (option == '2'):
            result = first_number - second_number
            print("O valor da substração é: ", result)
            print()

        if (option == '3'):
            result = first_number * second_number
            print("O valor da multiplicação é: ", result)
            print()

        if (option == '4'):
            if(second_number == 0):
                print("Divisão por 0 não é possível! Tente novamente.\n")
                continue
            else:
                result = first_number / second_number
                print("O valor da divisão é: ", result)
                print()

calculadora()
