import streamlit as st
import pandas as pd
import logic
import plotly.express as px

# 1. Configurazione Pagina
st.set_page_config(page_title="CompliancePro AI - Italia", layout="wide", page_icon="🛡️")

# 2. Sidebar di Navigazione
st.sidebar.title("🛡️ CompliancePro AI")
st.sidebar.markdown("---")
menu = st.sidebar.selectbox(
    "Menu Principale", 
    ["🏠 Dashboard Rischi", "📅 Scadenzario", "✍️ Generatore Documenti", "🤖 Analizzatore AI"]
)

# Recupero dati dal motore logic.py
scadenze = logic.get_scadenze_fittizie()
indice = logic.calcola_indice_rischio(scadenze)

# --- SEZIONE 1: DASHBOARD ---
if menu == "🏠 Dashboard Rischi":
    st.title("📊 Dashboard Conformità Normativa")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Indice di Conformità", f"{indice}%", delta=f"{indice-100}%", delta_color="inverse")
    col2.metric("Adempimenti Critici", "1", delta="Azione richiesta", delta_color="normal")
    col3.metric("Scadenze a 30gg", "1", help="Adempimenti che scadono entro il prossimo mese")

    st.markdown("---")
    
    df = pd.DataFrame(scadenze)
    fig = px.pie(df, names='Stato', title='Riepilogo Stato Normativo', 
                 color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig, use_container_width=True)

# --- SEZIONE 2: SCADENZARIO ---
elif menu == "📅 Scadenzario":
    st.title("📅 Registro Scadenze e Adempimenti")
    st.write("Elenco dettagliato delle scadenze normative per l'anno 2026.")
    
    df = pd.DataFrame(scadenze)
    
    def color_stato(val):
        color = '#ff4b4b' if val == 'Scaduto' else ('#ffa500' if val == 'In Scadenza' else '#28a745')
        return f'background-color: {color}; color: white; font-weight: bold'

    st.dataframe(df.style.applymap(color_stato, subset=['Stato']), use_container_width=True)

# --- SEZIONE 3: GENERATORE ---
elif menu == "✍️ Generatore Documenti":
    st.title("✍️ Generatore di Documentazione Legale")
    st.info("Compila i campi sottostanti per generare un documento conforme agli standard italiani.")
    
    with st.container():
        tipo_doc = st.selectbox("Cosa vuoi generare?", ["Informativa Privacy GDPR", "Documento Valutazione Rischi (Bozza)", "Certificazione Parità di Genere"])
        
        with st.form("form_documento"):
            c1, c2 = st.columns(2)
            nome_azienda = c1.text_input("Nome Ragione Sociale")
            sede = c2.text_input("Comune Sede Legale")
            responsabile = st.text_input("Nome Titolare / DPO")
            
            conferma = st.form_submit_button("Genera Documento Professionale")
        
        if conferma:
            if nome_azienda and sede and responsabile:
                doc_finale = logic.genera_informativa_privacy(nome_azienda, sede, responsabile)
                st.success("✅ Documento pronto per il download!")
                st.text_area("Anteprima del testo:", doc_finale, height=400)
                
                st.download_button(
                    label="📥 Scarica Informativa in formato TXT",
                    data=doc_finale,
                    file_name=f"Privacy_{nome_azienda}.txt",
                    mime="text/plain"
                )
            else:
                st.error("⚠️ Inserire tutti i dati richiesti per procedere.")

# --- SEZIONE 4: ANALIZZATORE ---
elif menu == "🤖 Analizzatore AI":
    st.title("🤖 AI Compliance Auditor")
    st.write("Carica un documento esistente per verificare se rispetta le attuali leggi italiane.")
    
    file = st.file_uploader("Trascina qui il file (PDF o Word)", type=["pdf", "docx"])
    
    if file:
        with st.spinner('Analisi in corso con motore AI...'):
            st.warning("🚩 Rilevata criticità: Il documento non menziona i tempi di conservazione dei dati (Art. 13 GDPR).")
            st.info("💡 Suggerimento: Integrare la sezione relativa ai diritti dell'interessato.")
