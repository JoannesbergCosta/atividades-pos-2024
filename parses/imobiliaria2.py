import json

with open('parses/imobiliaria.json') as imobiliaria_json:
    imobiliaria_data = json.load(imobiliaria_json)
print("")
print("MENU DE IMOVEIS")
qtd_elementos = len(imobiliaria_data['imobiliaria'])
print("")
for i in range(qtd_elementos):
    descricao = imobiliaria_data['imobiliaria'][i]['descricao']
    print(f'{i + 1} - {descricao}')
print("")

escolha = int(input('Digite o ID do imóvel para saber mais detalhes: '))

imovel = imobiliaria_data['imobiliaria'][escolha]

descricao = imovel['descricao']
nome = imovel['nome']
email = imovel.get('email', '')
telefone = imovel.get('telefone', '')
rua = imovel['rua']
bairro = imovel['bairro']
cidade = imovel['cidade']
numero = imovel.get('numero', '')
tamanho = imovel['tamanho']
numQuartos = imovel['numQuartos']
numBanheiros = imovel['numBanheiros']


print(f"Descrição: {descricao}")
print(f"Nome: {nome}")
if email:
    for a in email:
        print(f"Email: {a}")
if telefone:
    for b in telefone:
        print(f"Telefone: {b}")

print(f"Rua: {rua}")
print(f"Bairro: {bairro}")
print(f"Cidade: {cidade}")
print(f"Número: {numero}")
print(f"Tamanho: {tamanho}")
print(f"Número de Banheiros: {numBanheiros}")
print(f"Número de Quartos: {numQuartos}")

