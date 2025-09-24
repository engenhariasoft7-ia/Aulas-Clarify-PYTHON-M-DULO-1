executar = True

while executar:
    anoNasc =  int(input("Em que ano voce nasceu?"))
    anoAtual = int(input("Em que ano voce esta hoje?"))
    nome = input("Qual seu nome?")


    idade = anoAtual - anoNasc
    print(f"Ola {nome}, voce tem {idade} anos!")
    opcao = input("\nDeseja testar novamente? \nSim ou nao?") 
    if opcao == "não" or opcao== "Nao" or opcao == "n" or opcao == "nao":
        executar = False







       # https://servicodados.ibge.gov.br/api/docs
