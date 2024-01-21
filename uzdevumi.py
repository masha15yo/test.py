def tests(parametrs):
    a = parametrs #darbības ar parametriem
    return a #funkcijas rezultāts

# print(tests("kaķis"))

def pirmais(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

# print("The result is", pirmais(20,30) )

def otrais(): #def otrais(sakums = 0, beigas = 10, solis = 1)
    esosais = 0
    ieprieksejais = 0
    for i in range(10): #range(sakums, beigas, solis)
        ieprieksejais = esosais
        esosais = i
        summa = ieprieksejais+esosais
        print("Current Number", esosais, "Previous Number", ieprieksejais, "Sum:", summa)
    return

# otrais()

def tresais(teksts):
    print("Sākotnējais teksts ir ", teksts)
    print("Tikai pāra indeksa burti:")
    for i in range(0, len(teksts), 2):
        print(teksts[i])
    return

#tresais("pynative")

def ceturtais(teksts, n):
    print("Teksts:", teksts)
    print("Noņemot pirmos",n,"burtus sanāk:",teksts[n:])
    return

# ceturtais("pynative",4)

def piektais(saraksts):
    print("Dotais saraksts:", saraksts)
    print("Resultāts ir", saraksts[0]==saraksts[-1])
    return

skaitli1 = [10, 20, 30, 40, 10]
# skaitli2 = [75, 65, 35, 75, 30]

#piektais(skaitli1)


def sestais(saraksts):
    print("dotais saraksts:", saraksts)
    print("Ar 5 dalās:")
    for elements in saraksts:
        if elements%5 == 0:
            print(elements)
    return

# skaitli = [40, 65, 32, 88, 345, -5]
# sestais(skaitli)

def astotais(n):
    for i in range(1,n+1): # no 1 līdz n i mainīs vērtību
        for j in range (i):
            print(i, end = " ")
        print()
    return

astotais(8)

def devitais(skaitlis):
    teksta_forma = str(skaitlis)
    for i in range(len(teksta_forma)):
        if teksta_forma[i]!=teksta_forma[-1-i]:
            print("nav palindroms")
            return
    print("ir palindroms")
    return

# devitais("aka")

def desmitais(saraksts1, saraksts2):
    jaunais_saraksts = []
    for elements in saraksts1:
        if elements % 2 == 0:
            jaunais_saraksts.append(elements)
    for elements in saraksts2:
        if elements % 2 == 1:
            jaunais_saraksts.append(elements)
    print("pirmais saraksts:", saraksts1)
    print ("otrais saraksts:", saraksts2)
    print("apvienotais saraksts:", jaunais_saraksts)
    return

# sar1 = [13, 15, 132, 45, 88]
# sar2 = [42, 15, 123, 44, 93]
# desmitais(sar1, sar2)

def pedejais(n):
    for i in range(n, 0, -1):
        for j in range (i):
            print("*", end = " ")
        print()
    return

# pedejais(7)

def pedejais_ar_rekursiju(n):
    if n == 1:
        print("* ")
    else:
        print ("* "*n)
        pedejais_ar_rekursiju(n-1)

pedejais_ar_rekursiju(5)