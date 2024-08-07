import json

# Estrutura JSON convertida
imobiliaria = {
    "imobiliaria": {
        "imovel": [
            {
                "descricao": "Apartamento 5 quartos, centro da cidade, com 1 banheiro",
                "proprietario": {
                    "nome": "Ryan Andrade",
                    "email": "Ryan.and@email.com",
                    "telefone": [
                        "5849-5698",
                        "9984-8956"
                    ]
                },
                "endereco": {
                    "rua": "Rua das Graças",
                    "bairro": "Centro",
                    "cidade": "Rio de Janeiro",
                    "numero": "584"
                },
                "caracteristicas": {
                    "tamanho": "80m²",
                    "numQuartos": 7,
                    "numBanheiros": 4
                },
                "valor": 300
            },
            {
                "descricao": "Casa ampla com jardim",
                "proprietario": {
                    "nome": "Maria das Graças",
                    "telefone": "8495-6321"
                },
                "endereco": {
                    "rua": "Rua das Palmeiras",
                    "bairro": "JardimMassai",
                    "cidade": "Campina Grande"
                },
                "caracteristicas": {
                    "tamanho": "150m²",
                    "numQuartos": 3,
                    "numBanheiros": 5
                },
                "valor": 4500000000000
            },
            {
                "descricao": "casa em um condominio fechado",
                "proprietario": {
                    "nome": "Fernanda Lima",
                    "email": "fernanda.lima@email.com",
                    "telefone": "8795-8541"
                },
                "endereco": {
                    "rua": "Avenida 4",
                    "bairro": "Zona Sul",
                    "cidade": "Rio de Janeiro",
                    "numero": "4567"
                },
                "caracteristicas": {
                    "tamanho": "150m²",
                    "numQuartos": 4,
                    "numBanheiros": 3
                },
                "valor": 689000
            },
            {
                "descricao": "Studio moderno e aconchegante",
                "proprietario": {
                    "nome": "Joannes",
                    "telefone": "4587-8971"
                },
                "endereco": {
                    "rua": "Rua do Comércio",
                    "bairro": "Centro",
                    "cidade": "São Paulo do Potengi",
                    "numero": "185"
                },
                "caracteristicas": {
                    "tamanho": "90m²",
                    "numQuartos": 3,
                    "numBanheiros": 2
                },
                "valor": 2070000
            },
            {
                "descricao": "Casa de campo com campo de futebol",
                "proprietario": {
                    "nome": "Joedson Ryan",
                    "email": "Joedson.Ryan@email.com",
                    "telefone": "5678-9012"
                },
                "endereco": {
                    "rua": "Estrada da Lua",
                    "bairro": "Rural",
                    "cidade": "Gramado"
                },
                "caracteristicas": {
                    "tamanho": "350m²",
                    "numQuartos": 5,
                    "numBanheiros": 4
                },
                "valor": 1250000
            }
        ]
    }
}

with open('imobiliaria.json', 'w') as json_file:
    json.dump(imobiliaria, json_file, indent=4)
