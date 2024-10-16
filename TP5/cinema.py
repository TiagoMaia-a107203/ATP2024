def menu():
    print(""" -------------Menu---------------
          1- Listar as salas e os filmes respetivos
          2- Verificar se um lugar está disponível
          3- Vender o bilhete para um lugar disponível
          4- Listar a sala, o filme e o número de lugares disponíveis.
          5- Inserir uma nova sala ao cinema
          6- Remover uma sala
          7- Dar reset ao cinema
          8- Sair do menu
            """)
    
def existeSala(cinema, nome):
    cond=False
    for sala in cinema:
        if sala[3]== nome:
            cond =True 

    return cond

def listar(cinema):
    print("------------Lista de Filmes-------------")
    for s in cinema:
        nlugares, vendidos, filme, nome =s
        print(f"Sala:{nome}| Nome do filme:{filme}")
    print("------------------------------------------")
    return

def disponivel( cinema, filmes, lugar ):
    cond=False
    for s in cinema:
        nlugares, vendidos, filme, nome =s
        if filme==filmes and lugar <= nlugares:
            if lugar not in vendidos:
                cond= True
    return cond

def vendebilhete( cinema, filmes, lugar):
    if disponivel( cinema, filmes, lugar ):
        for s in cinema:
            nlugares, vendidos, filme, nome = s
            if filme == filmes:
                vendidos.append(lugar)
    else :
        print("Esse lugar já se encontra indisponível")
    return cinema

def listardisponibilidades(cinema):
    for s in cinema:
        nlugares, vendidos, filme, nome =s
        print(f"Sala: {nome}| Filme:{filme} |Nº de disponiveis:{nlugares-len(vendidos)}")
    return 

def inserirSala(cinema, nome, filme, nlugares):
    vendidos=[]
    s= (nlugares, vendidos, filme, nome)
    
    if not existeSala(cinema, nome):
        cinema.append(s)      
    else :
        print("Já existe uma sala com o mesmo nome!!")
    return cinema

def removeSala(cinema, nome_sala):
    for s in cinema:
        nlugares, vendidos, filme, nome=s
        if nome_sala == nome:
            cinema.remove(s)
    return cinema

cond2=True
cinema=[]
while cond2:
    menu()
    opcao = input("Introduza uma opção")

    while opcao not in ["1","2","3","4","5","6","7","8"]:
        print("Resposta inválida!! Tente novamente.")
        opcao=input("Introduza uma opção")

    if opcao== "1":
        listar(cinema)

    elif opcao=="2":
        filmes = input("Diga o filme que quer:")
        lugar= int(input("Diga o lugar que quer verificar se está disponível:"))        
        disponivel( cinema, filmes, lugar )
    
    elif opcao=="3":
        filmes = input("Diga o filme que quer:")
        lugar= int(input("Diga o lugar que quer verificar se está disponível:"))       
        print(vendebilhete( cinema, filmes, lugar))
        print("O lugar está vendido!!")
    
    elif opcao=="4":
        listardisponibilidades(cinema)

    elif opcao=="5":
        nome= input("Diga o nome da sala que quer ver se existe:")
        filme = input("Diga o filme que quer:")
        nlugares= int(input("Diga o número de lugares que quer que a sala tenha:"))
        print(inserirSala(cinema, nome, filme, nlugares))

    elif opcao=="6":
        nome_sala = input("Diga a sala que quer retirar:")
        removeSala(cinema, nome_sala)
        print("A sala foi retirada")
    
    elif opcao=="7":
        cinema.clear()
        print("O cinema sofreu um reset")
            
    elif opcao == "8":
        cond2 = False
print("Volte sempre!")
