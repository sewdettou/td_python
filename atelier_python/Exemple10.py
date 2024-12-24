#Gestionnairedetˆ aches(versionsimplifi´ ee)
taches = []
while True:
   action = input("Action (ajouter, afficher, quitter) : ")
   if action == "ajouter":
     tache = input("Entrez une t che : ")
     taches.append(tache)
     print(f"Tache ’{tache}’ ajoute.")
   elif action == "afficher":
     print("Taches :", taches)
   elif action == "quitter":
     print("Au revoir !")
     break
   else:
     print("Action inconnue.")