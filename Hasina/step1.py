# nom = input("saisir nom :")
# prenom = input("saisir prenom:")
# print("bonjour",nom,prenom)
# 
# def somme(a,b):
#     
#     return a+b
# 
# x = int(input("valeur de x: "))
# y = int(input("valeur de y: "))
# print(somme(x,y))
# a =int(input("sasir a:"))
# b =int(input("saisir b:"))
# c = int(input("saisir c:"))
# 
# if a<b<c or a<c<b:
#     print(a)
# elif b<a<c or b<c<a:
#     print(b)
# else:
#     print(c)
prix_HT = int(input("Entre le montant: "))

if prix_HT > 10000 :
    red = (prix_HT*15)/100
    prix_HT = prix_HT-red
    prix_TTC = prix_HT + (prix_HT * 0.2)
    print(prix_TTC)
    
else:
    prix_TTC = prix_HT + (prix_HT * 0.2)
    print(prix_TTC)