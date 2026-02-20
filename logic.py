import pandas as pd

def calcola_indice_rischio(dati_compliance):
    """Calcola la percentuale di conformità basata sugli adempimenti."""
    if not dati_compliance:
        return 0
    totale = len(dati_compliance)
    completati = sum(1 for item in dati_compliance if item['Stato'] == 'Conforme')
    return round((completati / totale) * 100, 1)

def get_scadenze_fittizie():
    """Ritorna la lista degli adempimenti per la dashboard."""
    return [
        {"Normativa": "GDPR - Registro Trattamenti", "Scadenza": "2026-03-15", "Stato": "In Scadenza", "Priorità": "Alta"},
        {"Normativa": "Sicurezza sul Lavoro (DVR)", "Scadenza": "2026-06-01", "Stato": "Conforme", "Priorità": "Media"},
        {"Normativa": "Certificazione ISO 9001", "Scadenza": "2026-01-10", "Stato": "Scaduto", "Priorità": "Critica"},
        {"Normativa": "AI Act - Autovalutazione", "Scadenza": "2026-05-20", "Stato": "Non Avviato", "Priorità": "Alta"},
    ]

def genera_informativa_privacy(nome_azienda, citta, responsabile):
    """Genera il testo legale per l'informativa privacy."""
    testo = f"""
    ============================================================
    INFORMATIVA PRIVACY AI SENSI DEL REGOLAMENTO UE 2016/679 (GDPR)
    ============================================================
    
    TITOLARE DEL TRATTAMENTO: {nome_azienda}
    SEDE LEGALE: {citta}
    RESPONSABILE PROTEZIONE DATI: {responsabile}
    
    1. OGGETTO DEL TRATTAMENTO
    Il Titolare tratta i dati personali, identificativi (ad esempio, nome, cognome, 
    ragione sociale, indirizzo, telefono, e-mail) comunicati dall'interessato.
    
    2. FINALITÀ DEL TRATTAMENTO
    I Suoi dati personali sono trattati senza il Suo consenso espresso per le 
    seguenti Finalità di Servizio:
    - Concludere i contratti per i servizi del Titolare;
    - Adempiere agli obblighi previsti dalla legge italiana e comunitaria.
    
    3. MODALITÀ DI TRATTAMENTO
    Il trattamento dei Suoi dati personali è realizzato per mezzo delle operazioni 
    indicate all’Art. 4 n. 2) GDPR.
    
    4. DIRITTI DELL’INTERESSATO
    Nella Sua qualità di interessato, ha i diritti di cui all’Art. 15 GDPR (Diritto di accesso, 
    rettifica, cancellazione, limitazione del trattamento, portabilità dei dati).
    
    ------------------------------------------------------------
    Documento generato da CompliancePro AI in data 20/02/2026.
    Il presente documento costituisce una bozza da sottoporre a revisione legale.
    ------------------------------------------------------------
    """
    return testo
