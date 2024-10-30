def menu():
    print(""" ------------Menu------------
    1- Média das temperturas por dia
    2- Guardar uma tabela de meteorologia
    3- Carregar uma tabela de meteorologia
    4- Identificar a temperatura mínima mais baixa
    5- Identificar as amplitudes das temperaturas por cada dia
    6- Identificar o dia de maior pluviosidade
    7- Identificar dias com pluviosidade maior que um limite
    8- Identificar o maior número de dias consecutivos com limite de pluviosidade
    9- Construir gráficos das temperaturas mínimas e máximas e um de pluviosidade
    0- Sair
            ----------------------------""")
    

def medias(tabMeteo):
    res = []
    for dia in tabMeteo:
        media = (dia[1] + dia[2])/2
        data = dia[0]
        res.append((data,media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, min, max, prec in t:
        ano, mes, dia = data
        registo =f"{ano}--{mes}--{dia}|{min}|{max}|{prec}\n"
        file.write(registo)
    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        #line = line[:-1]
        line = line.strip()
        campos = line.split("|")
        data, min, max, prec= campos
        ano, mes, dia = data.split("--")    
        tuplo = ((int(ano), int(mes), int(dia)), float(min), float(max), float(prec) )
        res.append(tuplo)
    file.close()
    return res

def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for dia in tabMeteo:
        if dia[1] < minima:
            minima = dia[1]
    return minima

def amplTerm(tabMeteo):
    res = []
    for dia in tabMeteo:
        amp= dia[2]-dia[1]
        data = dia[0]
        res.append((data, amp))
    return res 

def maxChuva(tabMeteo):
    max_data= tabMeteo[0][0]
    max_prec=tabMeteo[0][3]
    for dia in tabMeteo:
        if dia[3]> max_prec and dia[0] != max_data:
            max_prec=dia[3]
            max_data= dia[0]   
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res=[]
    for data, min, max, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
        
    return res

def maxPeriodoCalor(tabMeteo, p):
    consecutivos= 0
    consecutivos_global= 0
    for dias in tabMeteo:
        if tabMeteo[3] < p:
            consecutivos = consecutivos + 1
        else:
            if consecutivos > consecutivos_global:
                consecutivos_global = consecutivos
            consecutivos = 0

    if consecutivos > consecutivos_global:
        consecutivos_global = consecutivos
    return consecutivos_global

import matplotlib.pyplot as plt

def grafTabMeteo(t):
    datas = [f"{ano}--{mes}--{dia}" for (ano,mes,dia), *_ in t]
    temps_min = [min for data, min, *_ in t]
    temps_max= [max for data, min, max, *_ in t]
    precs= [prec for data, min, max, prec in t]
    
    
    plt.plot(datas, temps_min, label="Temp Mínima", color = "b", marker ="o")
    plt.plot(datas, temps_max, label= "Temperatura Máxima", color = "r", marker="o")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura Mínima")
    plt.legend()
    plt.show()

    plt.bar(datas, precs, label="Precipitação", color="c")
    plt.xlabel("Data")
    plt.ylabel("Precipitação mm")
    plt.title("Precipitação")
    plt.legend()
    plt.show()
    return

menu()
op= input("Introduza a opção que quer:")
while op != "0":
    while op not in ["0","1","2","3","4","5","6","7","8","9"]:
        print("Resposta inválida. Por favor introduza a opção novamente.")
        op= input("Introduza a opção que quer:")    
    if op == "1":
        print(f"A média das temperaturas foi de:{medias(tabMeteo1)}")
    elif op == "2":
        fnome = input("Introduza o nome do ficheiro que pretende usar:")
        guardaTabMeteo(tabMeteo1, fnome)
        print("O ficheiro foi gravado!")
    elif op == "3":
        fnome = input("Diga o ficheiro que quer carregar:")
        tabMeteo1 =carregaTabMeteo(fnome)
        print("O ficheiro que escolheu foi carregado!")
    elif op == "4":
        print(f"A temperatura mínima mais baixa registada foi {minMin(tabMeteo1)}")
    elif op == "5":
        print(f"A amplitude da temperatura em cada dia foi: {amplTerm(tabMeteo1)}")
    elif op == "6":
        print(f"A maior pluviosidade ocorreu no dia: {maxChuva(tabMeteo1)}")
    elif op == "7":
        p = float(input("Introduza o limite mínmimo de pluviosidade:"))
        print(f"Os dias em que a pluviosidade foi maior que {p} foram: {diasChuvosos(tabMeteo1, p)}")
    elif op == "8":
        p = float(input("Introduza o limite máximo de pluviosidade:"))
        print(f"O maior númerode dias consecutivos com pluviosidade abaixo de {p} foi {maxPeriodoCalor(tabMeteo1, p)}")
    elif op == "9":
        grafTabMeteo(tabMeteo1)
print("Volte sempre!!")
