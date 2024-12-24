chaine = str(input("Entrez une chaine de characteres : "))
c = str(input("Entrez une charactere : "))
s=0
for i in chaine:
    if i==c:
        s=s+1

print(s)
