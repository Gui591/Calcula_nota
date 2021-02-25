continuar = True


while (continuar != False):

    try:
        userEntry = int(input("Digite a opção que deseja\n[1] Consultar nota e [2] para sair: "))

        if (userEntry == 1):
            n1 = float(input("Digite a 1º nota da disciplina : "))
            n2 = float(input("Digite a 2º nota da disciplina : "))
            auxiliar_np1 = (n1+n2)/2

        elif (userEntry == 2):
            continuar = False
            print("Você digitou a opção sair, até mais !")
            break

        if (n1 > 10 and n2 > 10):
            print("Nota informada maior que 10, tente de novo\n")
              

        if (auxiliar_np1 >= 0 and auxiliar_np1 <= 6 ):
            print("Você foi reprovado na disciplina , sua nota foi {}\n".format(auxiliar_np1))

        elif (auxiliar_np1 >= 7 and auxiliar_np1 <= 10):
            print("Você foi aprovado na disciplina , sua nota foi {}\n".format(auxiliar_np1))


    except:
        print("Entrada inválida\n")



