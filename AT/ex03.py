def busca_contato(lista_contatos, nome):
    for contato in lista_contatos:
        if contato["nome"] == nome:
            return contato["telefone"]
    return None

contatos = [
    {"nome": "Alice", "telefone": "990612415"},
    {"nome": "Silvia", "telefone": "980712439"},
    {"nome": "Aline", "telefone": "547392459"},
    {"nome": "Gabriel", "telefone": "987653200"}
]

nome_buscado = "Alice"

telefone = busca_contato(contatos, nome_buscado)

if telefone is not None:
    print(f"{nome_buscado} - {telefone}.")
else:
    print(f"OPS... O contato {nome_buscado} não existe")

