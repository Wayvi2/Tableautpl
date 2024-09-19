import random


#Ex 1
def tableaucree():
    tableau = []
    for i in range(0,1000):
        a = random.randint(0,10)
        tableau.append(a)
    return tableau

#Ex 2

def occurence(x, tableau):
    count_tableau = 0
    for element in tableau:
        if x == element:
            count_tableau += 1
    return count_tableau

#Ex 3



tabCompteur = [0] * 10
# [0,0,0,0,0,0,0,0,0]

for i in range(0,1000):
    chiffre_hasard = random.randint(0, 10)
    tabCompteur[chiffre_hasard - 1] += 1

#for i in range(10):
    #print(f"Nombre {i+1} a été tiré {tabCompteur[i]} fois.")

#Ex 4

fib = [0,1]
for i in range (2,30):
    fib.append(fib[i-1] + fib[i-2])


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





##############
# Les tuples #
##############

#Ex 1
tup = ('b', 'o', 'n', 'j', 'o', 'u', 'r', ',', ' ', 'j', 'e', ' ', 'v', 'a', 'i', 's', ' ', 'b', 'i', 'e', 'n', ' ', 'e', 't', ' ', 'v', 'o', 'u', 's', '?')

def indice(car, tup):
    ind = 0
    while ind < len(tup) and tup[ind] != car:
        ind += 1
    if ind < len(tup):
        return ind
    else:
        return -1

print(indice('z',tup))



#Ex 2

def nbre_occurrences(car,tup):
    count = 0
    for i in tup:
        if i == car:
            count += 1
    return count

#Ex 3

def insere(car, indice, tup):
    lst = list(tup)
    lst.insert(indice, car)
    return tuple(lst)

def insere_correction(car, indice, tup):
    index = 0
    new_tup = ()
    if indice <= 0 or indice >= len(tup):
        return False
    else:
        for element in tup:
            if index == indice:
                new_tup += (car,)
            new_tup += (element,)
            index += 1
    return new_tup



#Ex 4

def supprime(indice, tup):
    new_tup = ()
    index = 0

    if 0 <= indice < len(tup):
        for element in tup:
            if index != indice:
                new_tup += (element,)
            index += 1
    return new_tup




#Ex 5

def renverse(tup):
    new_tup = ()
    index = len(tup) - 1

    while index >= 0:
        new_tup += (tup[index],)
        index -= 1
    return new_tup

print(renverse(tup))







