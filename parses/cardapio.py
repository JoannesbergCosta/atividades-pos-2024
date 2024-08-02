from xml.dom.minidom import parse
dom = parse("parses/cardapio.xml")

cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "livro"
pratos = cardapio.getElementsByTagName('prato')

id_prato = 0
# Acessa as informações de cada livro
for prato in pratos:
    id_prato+=1
    nome = prato.getElementsByTagName('nome')[0]
    ingredientes = prato.getElementsByTagName('ingredientes')[0]
    print(f'{id_prato} - {nome}')

id_p = int(input("Digite o id do prato para saber mais: "))
print("---\n")

prato = pratos[id_p-1]
nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
ingredientes = prato.getElementsByTagName('ingredientes')[0].firstChild.nodeValue

print(nome)
print(ingredientes)
