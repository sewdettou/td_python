#Programme de conversion de devises
taux_conversion = {"USD": 1.1, "MRO": 40.0, "MAD": 11.0}
devise = input("Entrez la devise cible (USD, MRO, MAD) : ")
if devise in taux_conversion:
   montant_euros = float(input("Entrez le montant en euros : "))
   montant_converti = montant_euros * taux_conversion[devise]
   print(f"{montant_euros} EUR = {montant_converti:.2f} {devise}")
else:
    print("Devise non supportee.")