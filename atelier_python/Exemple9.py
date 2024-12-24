#Dictionnairedescapitales
capitales = {"France": "Paris", "Mauritanie": "Nouakchott", "Espagne": "Madrid"}
pays = input("Entrez un pays : ")
if pays in capitales:
    print(f"La capitale de {pays} est {capitales[pays]}.")
else:
    print("Pays non trouv dans la base.")