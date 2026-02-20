import streamlit as st
import pandas as pd
import logic
import plotly.express as px

# Configurazione professionale
st.set_page_config(page_title="CompliancePro AI", layout="wide")

# Sidebar per navigazione
st.sidebar.title("🛡️ CompliancePro AI")
st.sidebar.info("Dashboard di monitoraggio normativo v1.0")
menu = st.sidebar.selectbox("Navigazione", ["🏠 Dashboard Rischi", "📅 Scadenzario", "🤖 Analizzatore AI", "📂 Archivio Documenti"])

# Dati di esempio
scadenze = logic.get_scadenze_fittizie()
indice = logic.calcola_indice_rischio(scadenze)

if menu == "🏠 Dashboard Rischi":
    st.title("📊 Stato della Compliance Aziendale")
    
    # Metriche principali
    col1, col2, col3 = st.columns(3)
    col1.metric("Indice di Conformità", f"{indice}%", delta=f"{indice-100}%", delta_color="inverse")
    col2.metric("Adempimenti Critici", "1", delta="Azione richiesta", delta_color="normal")
    col3.metric("Prossima Scadenza", "15 Mar", delta="GDPR")

    st.write("---")
    
    # Grafico a torta degli stati
    df = pd.DataFrame(scadenze)
    fig = px.pie(df, names='Stato', title='Distribuzione Stato Adempimenti', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

elif menu == "📅 Scadenzario":
    st.title("📅 Registro Scadenze Normative")
    df = pd.DataFrame(scadenze)
    
    # Formattazione colori per tabella
    def color_stato(val):
        color = 'red' if val == 'Scaduto' else ('orange' if val == 'In Scadenza' else 'green')
        return f'color: {color}; font-weight: bold'

    st.table(df.style.applymap(color_stato, subset=['Stato']))

elif menu == "🤖 Analizzatore AI":
    st.title("🤖 AI Compliance Auditor")
    st.write("Carica un contratto o un'informativa per verificare la conformità con l'AI Act o GDPR.")
    
    uploaded_file = st.file_uploader("Scegli un file (PDF o DOCX)", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        with st.spinner('L\'intelligenza artificiale sta analizzando il documento...'):
            # Qui in futuro collegheremo l'API di Gemini o OpenAI
            st.warning("⚠️ Rilevata clausola potenzialmente non conforme a pag. 3 (Gestione Dati Terzi)")
            st.success("✅ Struttura generale conforme agli standard ISO.")
