def moyenne(notes):
    """Calcule la moyenne d'une liste de notes (retourne 0 si vide)."""
    if not notes:
        return 0
    return sum(notes) / len(notes)


def appliquer_bonus(notes, bonus=1):
    """Renvoie une nouvelle liste avec un bonus, limité à 20."""
    return [min(note + bonus, 20) for note in notes]


def filtrer_notes(notes, seuil):
    """Conserve uniquement les notes ≥ seuil."""
    return [note for note in notes if note >= seuil]


def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes"):
    """Génère un rapport texte regroupant les infos principales."""
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)

    lignes = [
        
        f"Notes originales : {notes}",
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Notes ≥ {seuil} : {notes_valides} (total {len(notes_valides)})"
    ]
    return "\n"



def trouver_extremes(notes):
    """Trouve la note minimale et maximale."""
    if not notes:
        return None, None
    return min(notes), max(notes)


if __name__ == "__main__":
    
    notes = [12, 9, 15, 8, 17, 13, 19, 10]
    
    print(" TEST PRINCIPAL ")
    print(rapport(notes))
    
    
    
    print(" RAPPORT AVANCÉ ")
    print(rapport(notes, bonus=2, seuil=14, titre="Rapport avancé"))
    
    
    
    print(" TESTS INDIVIDUELS ")
    
    print(f"Notes originales : {notes}")
    print(f"Moyenne : {moyenne(notes):.2f}")
    
    notes_bonus = appliquer_bonus(notes, bonus=1)
    print(f"Notes avec bonus de 1 : {notes_bonus}")
    print(f"Moyenne avec bonus : {moyenne(notes_bonus):.2f}")
    
    notes_filtrees = filtrer_notes(notes, seuil=15)
    print(f"Notes ≥ 15 : {notes_filtrees}")
    print(f"Nombre de notes ≥ 15 : {len(notes_filtrees)}")
    
    min_note, max_note = trouver_extremes(notes)
    print(f"Note minimale : {min_note}")
    print(f"Note maximale : {max_note}")
    
    
    
    print(" TEST AVEC LISTE VIDE ")
    notes_vides = []
    print(f"Liste vide : {notes_vides}")
    print(f"Moyenne liste vide : {moyenne(notes_vides)}")
    print(f"Notes filtrées (≥10) : {filtrer_notes(notes_vides, 10)}")
    print(f"Notes avec bonus : {appliquer_bonus(notes_vides, 5)}")
    
    
    
    print(" RAPPORT PERSONNALISÉ ")
    
    notes_classe_B = [14, 11, 16, 9, 18, 12, 7, 20, 15]
    rapport_perso = rapport(
        notes_classe_B,
        bonus=1.5,
        seuil=10,
        titre="Rapport de la classe B - Semestre 2"
    )
    print(rapport_perso)