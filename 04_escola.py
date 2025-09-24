
tipoEscola = input("Estuda em colegio: \n [1] Publico\n[2]Particular\n")
nomeAluno = input('qual o nome do aluno?')
mediaAluno = int(input("Qual a media do aluno?" + nomeAluno + "?\n" ))
freqAluno = int(input("Qual a media do aluno?" + nomeAluno + "?\n" ))

'''
!= diferente
== igual
<= menor ou igual
>= maior ou igual
< menor
> maior
'''


if tipoEscola == "2":
    print("------------Escola Particular-----------")
    if mediaAluno >= 7 and freqAluno >= 70:
            status = "Aprovado"
    else:
        statu = 'Reprovado'

if tipoEscola == "1":
    print("------------Escola Publica---------------")
    if mediaAluno >= 6 or freqAluno >= 70:
     status ="Aprovado"
    else:
     status = "Reprovado"            

   
print(f"O Aluno {nomeAluno} foi  {status}  com media   {mediaAluno}")       