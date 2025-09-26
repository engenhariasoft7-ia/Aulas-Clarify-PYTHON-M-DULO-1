def divisao(a , b):

    try:
        resultado = a / b
        print(f"O resultado da divisão de {a} e {b} é: {resultado}")

    except ZeroDivisionError:
        print("Erro: Tentou dividir por 0? ta errado rapaz!")

    except TypeError:
        print("Erro: Não da pra dividir textos")
            
    except Exception as descricao:
        print(f"É um erro Inesperado: {descricao}")

    else:
        print("Divisão realizada com sucesso!")

    finally:print("Processo de divisão concluido!")           

divisao(10,2)
divisao(10,0)
divisao(10,"dois")
divisao("10",2)        