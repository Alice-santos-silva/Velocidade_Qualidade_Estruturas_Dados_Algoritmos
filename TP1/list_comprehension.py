def list_comprehension():
    string = "Sítio do pica-pau amarelo \n 2023"
    caracteres = [char for char in string if not char.isspace()]
    return caracteres
