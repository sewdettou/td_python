#Calcul de la somme des nombres pairs
limite = int(input("Entrez un nombre : "))
somme = 0
for i in range(2, limite + 1, 2):
    somme += i
    print(f"La somme des nombres pairs jusqu’ {limite} est {somme}.")