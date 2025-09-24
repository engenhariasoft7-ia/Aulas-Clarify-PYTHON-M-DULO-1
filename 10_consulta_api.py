import json, requests

#https://colab.research.google.com/
#https://app.inventor.mit.edu/

resposta = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/byanca")

json_dados = json.loads(resposta.text)
print(json_dados[0]['res'][2])