import conexao
from za import validar_titulo


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
    nome = input("Digite Seu nome completo: ").strip()

    titulo_eleitor = input("Digite seu titulo de eleitor: ").strip()
    titulo_eleitor = titulo_eleitor.replace(" ", "")
    if not validar_titulo(titulo_eleitor):
        print ("Título inváldo. Cadastro não realizado.")
        return


    cpf = input("Digite seu CPF: ").strip()
    cpf = cpf.replace(".", "").replace("-", "")

    
    if not validar_cpf(cpf):
        print("CPF inválido. Cadastro não realizado.")
        return  

    print("CPF válido.")

    chave_acesso = input("Digite sua chave de acesso: ").strip()

    mesario = input("Você atuará como mesário? (SIM) ou (NÃO): ").strip().upper()
    valor_mesario = True if mesario == "SIM" else False

    status = input("Digite o status: ").strip().capitalize()

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









