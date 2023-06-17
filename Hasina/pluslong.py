nom = str(input("Nom 1: "))
noms = str(input("Nom 2: "))

n1 = len(nom)
n2 = len(noms)

#Les conditions
if n1<n2:
    print("Le mot le plus long est",noms)
elif n1>n2:
    print("Le mot le plus long est",nom)
else :
    print("Les deux mot on de même longueur")