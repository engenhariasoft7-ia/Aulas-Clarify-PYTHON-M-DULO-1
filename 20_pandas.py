import pandas as pd
#pip install pandas
data = {
    'Nome':['Juliana', 'Byanca', "Diogo",'Marcelo', 'Emanuel', 'Horacio'],
    'Idade':[12,22,32,44,45,21],
    'Salario':[5000,6000,7000,8000,9000,4000]       
}

df = pd.DataFrame(data)

print('Conteudo do DataFrame:')
print(df)

#selecionando apenas um, a coluna
print('\n Coluna de Nome:')
print( df['Nome'] )

#filtrando linhas
print('\n Pessoas com Idade menor que 30')
print(df[ df['Idade'] < 30])

# calculando imposto e adicionando uma nova coluna
df['Imposto'] = df['Salario'] * 0.1
print
("\n Nova coluna de imposto")
print(df)

media_salario = df['Salario'].mean()
print('\n Média Salarial:')
print(media_salario)

# Salvando o dataframe em um arquivo CSV
df.to_csv(r'C:\Users\integral\Desktop\PythonByanca\Pandas.csv', index=False)

leitura = pd.read_csv
(r'C:\Users\integral\Desktop\PythonByanca\Pandas.csv')

print('\nTabela importada do arquivo CVS:')
print(leitura)