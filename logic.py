import pandas as pd

def calcola_indice_rischio(dati_compliance):
    """Calcola una percentuale di rischio basata sugli adempimenti completati."""
    totale = len(dati_compliance)
    completati = sum(1 for item in dati_compliance if item['Stato'] == 'Conforme')
    percentuale = (completati / totale) * 100
    return round(percentuale, 1)

def get_scadenze_fittizie():
    """Ritorna una lista di scadenze normative per il prototipo."""
    return [
        {"Normativa": "GDPR - Registro Trattamenti", "Scadenza": "2026-03-15", "Stato": "In Scadenza", "Priorità": "Alta"},
        {"Normativa": "Sicurezza sul Lavoro (DVR)", "Scadenza": "2026-06-01", "Stato": "Conforme", "Priorità": "Media"},
        {"Normativa": "Certificazione ISO 9001", "Scadenza": "2026-01-10", "Stato": "Scaduto", "Priorità": "Critica"},
        {"Normativa": "AI Act - Autovalutazione", "Scadenza": "2026-05-20", "Stato": "Non Avviato", "Priorità": "Alta"},
    ]
