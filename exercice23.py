nombre=int(input("Donner un nombre SVP : "))

somme=0

for i in range(1,nombre+1):
    somme=somme+(1/i)

print("la somme est ",somme)