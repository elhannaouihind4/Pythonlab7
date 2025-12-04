def calcul_ttc(prix_ht, taux=0.2):
    prix_ttc = prix_ht * (1 + taux)
    return prix_ttc

print(calcul_ttc(100))           # utilise le taux par défaut (20 %)
print(calcul_ttc(100, 0.055))    # nouveau taux
print(calcul_ttc(prix_ht=50, taux=0.1))  # arguments nommés