
def moyenne(notes):
    """Calcule la moyenne d'une liste de notes (retourne 0 si vide)."""
    if not notes:
        return 0
    return sum(notes) / len(notes)


def min_max(notes):
    """Retourne un tuple (note minimale, note maximale)."""
    if not notes:
        return None, None
    return min(notes), max(notes)


def normaliser(notes, sur=20):
    """
    Ramène toutes les notes sur 20.
    Exemple: [50, 75, 100] sur 100 -> [10, 15, 20] sur 20
    """
    if not notes:
        return []
    
    
    max_note = max(notes)
    
    
    if max_note <= 20:
        return notes.copy()
    
    
    coefficient = sur / max_note
    return [note * coefficient for note in notes]


def appliquer_bonus(notes, bonus=1):
    """Renvoie une nouvelle liste avec un bonus, limité à 20."""
    return [min(note + bonus, 20) for note in notes]


def filtrer_notes(notes, seuil):
    """Conserve uniquement les notes ≥ seuil."""
    return [note for note in notes if note >= seuil]






def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes", normaliser_sur=None):
    """
    Génère un rapport texte regroupant les infos principales.
    Si normaliser_sur est spécifié, normalise les notes avant traitement.
    """
    
    if normaliser_sur is not None:
        notes_originales = notes.copy()  
        notes = normaliser(notes, normaliser_sur)
    else:
        notes_originales = notes.copy()
    
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)
    note_min, note_max = min_max(notes)
    
    lignes = [
        f"=== {titre} ===",
        f"Notes originales : {notes_originales}" + 
          (f" (normalisées sur {normaliser_sur} → {notes})" if normaliser_sur is not None else ""),
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Note minimale : {note_min if note_min is not None else 'N/A'}",
        f"Note maximale : {note_max if note_max is not None else 'N/A'}",
        f"Écart : {note_max - note_min if note_min is not None and note_max is not None else 'N/A'}",
        f"Notes ≥ {seuil} : {notes_valides} (total {len(notes_valides)})",
        f"Taux de réussite : {len(notes_valides)/len(notes)*100:.1f}%" if notes else "Taux de réussite : N/A"
    ]
    






def sauvegarder_rapport(notes, nom_fichier="rapport_notes.txt", **kwargs):
    """
    Génère un rapport et le sauvegarde dans un fichier.
    **kwargs : paramètres optionnels pour la fonction rapport()
    """
    rapport_texte = rapport(notes, **kwargs)
    
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(rapport_texte)
    
    print(f" Rapport sauvegardé dans '{nom_fichier}'")
    return nom_fichier




if __name__ == "__main__":
    
    print("TEST DES NOUVELLES FONCTIONS")
    
    
    
    notes_test = [12, 9, 15, 8, 17, 13, 19, 10]
    print(f"\n1. Test de min_max sur {notes_test}")
    minimum, maximum = min_max(notes_test)
    print(f"   → Min: {minimum}, Max: {maximum}")
    
    
    notes_sur_100 = [50, 75, 100, 25, 60]
    print(f"\n2. Test de normaliser sur {notes_sur_100} (sur 100)")
    notes_normalisees = normaliser(notes_sur_100, 20)
    print(f"   → Normalisées sur 20: {notes_normalisees}")
    
    
    print(f"   → Vérification: 50/100*20 = {50/100*20:.1f}, 75/100*20 = {75/100*20:.1f}")
    
    
    print(f"\n3. Test de normaliser sur {notes_test} (déjà sur 20)")
    notes_non_normalisees = normaliser(notes_test, 20)
    print(f"   → Résultat: {notes_non_normalisees} (devrait être identique)")
    
    
    print("MINI-PROJET COMPLET")
    
    
    
    print("\n SCÉNARIO 1 : Notes sur 20")
    notes_classe_A = [12, 9, 15, 8, 17, 13, 19, 10]
    rapport_A = rapport(notes_classe_A, bonus=1, seuil=12, titre="Classe A - Mathématiques")
    print(rapport_A)
    
    
    sauvegarder_rapport(notes_classe_A, "rapport_classe_A.txt", 
                       bonus=1, seuil=12, titre="Classe A - Mathématiques")
    

    
    
    print("\n SCÉNARIO 2 : Notes sur 100 normalisées sur 20")
    notes_classe_B = [50, 75, 100, 25, 60, 85, 90, 45]
    rapport_B = rapport(notes_classe_B, bonus=1.5, seuil=12, 
                       titre="Classe B - Physique (sur 100)", normaliser_sur=100)
    print(rapport_B)
    
    
    sauvegarder_rapport(notes_classe_B, "rapport_classe_B.txt",
                       bonus=1.5, seuil=12, 
                       titre="Classe B - Physique (sur 100)", 
                       normaliser_sur=100)
    
    
    
    
    print("\n📊 SCÉNARIO 3 : Liste vide")
    notes_vides = []
    rapport_vide = rapport(notes_vides, titre="Classe vide")
    print(rapport_vide)
    
    
    
    
    print("\n SCÉNARIO 4 : Notes sur 40")
    notes_sur_40 = [32, 28, 35, 18, 40, 25, 38, 30]
    rapport_40 = rapport(notes_sur_40, bonus=2, seuil=15,
                        titre="Classe C - Chimie (sur 40)", normaliser_sur=40)
    print(rapport_40)
    
    
    print("FICHIERS CRÉÉS :")
    
    print("1. rapport_classe_A.txt")
    print("2. rapport_classe_B.txt")
    print("\nOuvre ces fichiers pour voir les rapports sauvegardés !")