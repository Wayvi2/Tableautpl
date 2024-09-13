import random

#Ex 1
def tableaucree():
    tableau = []
    for i in range(0,1000):
        a = random.randint(0,10)
        tableau.append(a)
    return tableau
print(tableaucree())

#Ex 2

def occurence(x, tableau):
    count_tableau = 0
    for element in tableau:
        if x == element:
            count_tableau += 1
    return count_tableau
print(occurence(6,tableaucree()))

#Ex 3



tabCompteur = [0] * 10
# [0,0,0,0,0,0,0,0,0]

for i in range(0,1000):
    chiffre_hasard = random.randint(0, 10)
    tabCompteur[chiffre_hasard - 1] += 1

for i in range(10):
    print(f"Nombre {i+1} a été tiré {tabCompteur[i]} fois.")

#Ex 4

fib = [0,1]
for i in range (2,30):
    fib.append(fib[i-1] + fib[i-2])
print(fib[29])


#Ex 5

def doublons(T):
    for i in range(len(T)):
        for j in range(i+1,len(T)):
            if T[i] == T[j]:
                return True
    return False

#Ex 6

def echange(tab,i,j):
    tab[i], tab[j] = tab[j], tab[i]
    return tab

#EX 7

def miroir(tab):
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            echange(tab,i,j)
    return tab

def miroir_correction(tab):
    for i in range (len(tab)//2):
        echange(tab,i,-i-1)
    return

tab = [0,1,2,3]
print(miroir(tab))

#Ex 8
def melange(tab):
    for i in tab:
        chiffre_hasard = random.randint(0, len(tab)-1)
        echange(tab,i,chiffre_hasard)
    return tab

#Ex 9

def hamming(tab1,tab2):
    count = 0
    for i in range(len(tab1)):
        if tab1[i] != tab2[i]:
            count += 1
    return f"Il y a {count} index différent"





