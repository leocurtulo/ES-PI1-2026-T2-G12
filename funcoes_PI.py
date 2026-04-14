def validar_cpf(cpf):
    if len(cpf) != 11:
        return False       
    for c in cpf:
        if c < '0' or c > '9':
            return False

    return True


def cadastro_eleitores():
    nome = input("Digite Seu nome completo:")
    titulo_eleitor = input("Digite seu titulo de eleitor:")
    cpf = input("Digite seu CPF: ")
    mesario = input("Você atuará como mesário? (SIM) ou (NÃO): ").upper()

    if validar_cpf(cpf):
        print("CPF válido")
    else:
        print("CPF inválido")


cadastro_eleitores()
      










