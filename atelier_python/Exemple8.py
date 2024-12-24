#Calcul du carr´e d’un nombre
def carre(nombre):
   return nombre ** 2
nb = int(input("Entrez un nombre : "))
print(f"Le carr de {nb} est {carre(nb)}.")