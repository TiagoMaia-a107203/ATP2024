def menu():
    print(""" ------------Menu------------
    1- Criar Turma
    2- Inserir Aluno
    3- Listar a Turma
    4- Consultar Aluno por ID
    5- Guardar a turma num ficheiro
    6- Carregar uma turma dum ficheiro
    0- Sair
            ----------------------------""")


def inserirAl(turma, id, nome, notas):
    tpc = int(input("Quanto teve no TPC?"))
    notas.append(tpc)
    projeto = int(input("Quanto teve no projeto?"))
    notas.append(projeto)
    teste = int(input("Quanto teve no teste?"))
    notas.append(teste)
    aluno = (nome, id, notas)
    turma.append(aluno)
    return turma

def listaTurma(turma, nome_turma):
    print(f"---------------{nome_turma}---------------")
    for aluno in turma:
        nome, id, notas = aluno
        print(f" Aluno:{nome}; ID:{id}; Notas:{notas}")
    print("-------------------------------------------")
    return

def existeAluno(turma, id):
    cond = False
    for aluno in turma:
        if aluno[1] == id:
            cond = True
    return cond

def consultarAluno(turma, id):
    if existeAluno(turma, id):
        for aluno in turma:
            nome, idt, notas = aluno
            if id == idt:
                print(f" Aluno:{nome}; ID:{idt}; Notas: {notas}")
    else:
        print("Não existe um aluno com esse id.")
    return

def guardarFicheiro(turma, nome_ficheiro):
    file = open(f"./aula_6/{nome_ficheiro}.txt","w")
    for aluno in turma:
        nome, idt, notas = aluno 
        tpc, projeto, teste = notas
        registo =f"{nome}|{idt}|{tpc}|{projeto}|{teste}\n"
        file.write(registo)
    file.close()

def buscarficheiro(turma, nome_ficheiro):
    file = open(f"./aula_6/{nome_ficheiro}.txt")
    for linha in file:
        campos = linha.split("|")
        campos1 = [int(campos[2]), int(campos[3]), int(campos[4])]
        aluno = (campos[0], campos[1], campos1)
        turma.append(aluno)
    return turma


opcao = "1"
while opcao != "0":
    menu()
    opcao = input("Opcao:")
    if opcao == "1":
        nome_turma1 = input("Diga o nome da turma:")
        turma_nova = []
        print("Turma criada!")
    elif opcao == "2":
        nome = input("Introduza o nome do aluno:")
        idtd = input("Introduza o id do aluno:")
        notas = []
        turma = inserirAl(turma_nova, idtd, nome, notas)
    elif opcao == "3":
        listaTurma(turma_nova, nome_turma1)
    elif opcao == "4":
        id2 = input("Qual o id do aluno que quer consultar?")
        consultarAluno(turma_nova, id2)
    elif opcao == "5":
        guardarFicheiro(turma_nova, nome_turma1)
        print("Ficheiro guardado!")
    elif opcao == "6":
        nomef = input("Qual o ficheiro que deseja carregar?")
        nome_turma1 = nomef
        turma_nova.clear()
        buscarficheiro(turma_nova, nomef)
        print("Ficheiro carregado!")
