nom1=str(input("saisir premiere nom: "))
nom2=str(input("saisir deuxieme nom: "))
n=len(nom1)
m=len(nom2)
if n>m:
    print(nom1)
elif m>n:
    print(nom2)
else:
    print(nom1)
    print(nom2)
