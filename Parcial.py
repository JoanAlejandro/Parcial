precioa=5
preciob=10
precioc=15
print("PROGRAMA DE PRACTICA\n")
print("A- Manzana $5 \nB-Pera $10 \nC-Naranja $15")
a=int(input("Digite cuantas Manzanas quiere: "))
b=int(input("Digite cuantas Peras quiere: "))
c=int(input("Digite cuantas Naranjas quiere: "))

if a<=5:
    valor=a*precioa
elif a>5 or a<=10:
    print