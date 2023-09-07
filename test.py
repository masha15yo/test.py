from inspect import isgetsetdescriptor


def tests(parametrs):
    a = parametrs #darbibas ar parametriem 
    return a #funkcijas rezultats

#print(tests("kaķis"))

def pirmais(par1, par2):
    reizinajums = par1*par2 
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

#print("The result is", pirmais(40,30) )

def otrais():  #sakums = 0, beigas = 10, solis = 1
    esosais = 0
    ieprieksejais = 0
    for i in range(10): #sakums, beigas, solis
        ieprieksejais = esosais
        esosais = i
        summa = ieprieksejais+esosais
        print("Current Number", esosais, "Previous Number", ieprieksejais, "Sum:", summa)
    return

#otrais() #0, 10, 1

def tresais(teksts):
    print("Sākotnējais teksts ir ", teksts)
    print("Tikai pāra indeksa burti:")
    for i in range(0, len(teksts), 2):
        print (teksts[i])
    return

tresais("pynative")

def ceturtais(teksts, n):
    print("Teksts:", teksts)
    print("Noņemt pirmos", n, "burtus sanāk:", teksts[n:])
    return

#ceturtais("pynative",4)

def piektais(saraksts):
    print("Dotais saraksts", saraksts)
    print("Result is", saraksts[0]==saraksts[-1])
    return

skaitli1 = [10,20,30,40,10]
skaitli2 = [75,65,35,75,30]

piektais(skaitli1)