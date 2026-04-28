import conexao



def validar_cpf(cpf):
    cpf = cpf.strip()
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    if len(cpf) != 11:
        return False       
    elif not cpf.isdigit():
        return False
    elif cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range (9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma  % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1= (11 - resto)

    soma = 0
    for i in range (10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = (11 - resto)
    if digito2 >= 10:
        digito2 = 0


    return cpf[9] == str(digito1) and cpf[10] == str(digito2)


def cadastro_eleitores():
    nome = input("Digite Seu nome completo:")
    nome = nome.strip()

    titulo_eleitor = input("Digite seu titulo de eleitor:")
    titulo_eleitor = titulo_eleitor.strip()
    titulo_eleitor = titulo_eleitor.replace(" ", "")


    cpf = input("Digite seu CPF: ")
    cpf = cpf.strip()
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")

    chave_acesso = input ("Digite sua chave de acesso: ")
    chave_acesso = chave_acesso.strip()

    mesario = input("Você atuará como mesário? (SIM) ou (NÃO): ").upper()
    mesario = mesario.strip()

    status = input ("Digite o status: ")
    status = status.strip()
    status = status.capitalize()

    if validar_cpf(cpf):
        print("CPF válido")
        if mesario == "SIM":
            valor_mesario = True
        else:
            valor_mesario = False
        
        sql = """
        INSERT INTO eleitores 
        (cpf, nome_completo, titulo_eleitor, chave_acesso, is_mesario, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            cpf,
            nome,
            titulo_eleitor,
            chave_acesso,
            valor_mesario,
            status
        )

        conexao.cursor.execute(sql, valores)
        conexao.conexao.commit()
        print("Eleitor cadastrado com sucesso!")

    else:
        print("CPF inválido")





def buscar_eleitor():

    cpf = input("Digite o CPF para buscar: ")
    cpf = cpf.strip()
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")


    sql = "SELECT * FROM eleitores WHERE cpf = %s"

    valores = (cpf,)

    conexao.cursor.execute(sql, valores)

    resultado = conexao.cursor.fetchone()

    if resultado:
        print("Eleitor encontrado:")
        print(resultado)
    else:
        print("Eleitor não encontrado")









