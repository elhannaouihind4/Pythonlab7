def somme(*args):
    total = 0
    for valeur in args:
        total += valeur
    return total

print(somme(1, 2))
print(somme(1, 2, 3, 4))

def produit(*args):
    resultat = 1  
    for valeur in args:
        resultat *= valeur  
    return resultat


print("produit(2, 3) =", produit(2, 3))  
print("produit(1, 2, 3, 4) =", produit(1, 2, 3, 4))  
print("produit(5) =", produit(5))  
print("produit() =", produit())  


print("produit(2, 2, 2) =", produit(2, 2, 2))  
print("produit(10, 0.5) =", produit(10, 0.5))  


def afficher_args(*args):
    print(f"Type de args: {type(args)}")
    print(f"Contenu de args: {args}")
    print(f"Longueur de args: {len(args)}")

print("\nAnalyse de *args :")
afficher_args(1, 2, 3)
afficher_args()  