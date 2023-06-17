n= int(input("Le nombre d'element du tableau: "))
tab = []
for i in range(n):
    m= int(input("Element n°{} :".format(i+1)))
    tab.append(m)
'''
j=n-1
while j>=0:
    print(tab[j],end=' ')
    j-=1
'''
tab.reverse()
print(tab)