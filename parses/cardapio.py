from xml.dom.minidom import parse

# Carrega o arquivo XML
dom = parse("parses/cardapio.xml")
cardapio = dom.documentElement

# Obtém a lista de pratos
pratos = cardapio.getElementsByTagName('prato')

# Exibe os pratos
for i, prato in enumerate(pratos, 1):
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    print(f'{i} - {nome}')

# Solicita o ID do prato ao usuário
try:
    id_p = int(input("Digite o ID do prato para saber mais: "))
    prato = pratos[id_p - 1]
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    ingrediente = prato.getElementsByTagName('ingrediente')[0].firstChild.nodeValue

    print("---\n")
    print(f'Nome: {nome}')
    print(f'Ingredientes: {ingrediente}')
except (IndexError, ValueError):
    print("ID inválido. Verifique o ID e tente novamente.")
