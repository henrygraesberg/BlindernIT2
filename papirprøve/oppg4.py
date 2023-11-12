def kamp_resultat(home: str, away: str, h_score: int, a_score: int):
    if h_score > a_score:
        return "Hjemmelag"
    if a_score > h_score:
        return "Bortelag"
    return "Uavgjort"

print(kamp_resultat("Vålerenga", "HamKam", 5, 0))