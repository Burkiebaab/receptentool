import streamlit as st
import requests

# --- CONFIGURATIE ---
# Vervang dit door jouw unieke n8n Webhook URL
N8N_WEBHOOK_URL = http://localhost:5678/webhook-test/79c291a7-6f30-4cc5-a39f-536cefd0c6ce

st.set_page_config(page_title="GA4 & Recepten AI Agent", page_icon="📊")

st.title("🤖 AI Data & Recepten Agent")
st.markdown("Stel een vraag over je GA4 data of kies een van de snelle opties hieronder.")

# --- FUNCTIE OM N8N AAN TE ROEPEN ---
def query_n8n(prompt):
    with st.spinner("De AI denkt na..."):
        try:
            # We sturen de prompt naar n8n via een POST request
            response = requests.post(N8N_WEBHOOK_URL, json={"chatInput": prompt})
            response.raise_for_status()
            return response.text # Of response.json() afhankelijk van je Respond to Webhook instelling
        except Exception as e:
            return f"Oeps! Er ging iets mis: {e}"

# --- DE TWEE RECEPT KNOPPEN ---
col1, col2 = st.columns(2)

with col1:
    if st.button("🥦 Vegetarisch recept"):
        resultaat = query_n8n("Geef me een vegetarisch recept")
        st.session_state['last_response'] = resultaat

with col2:
    if st.button("🥩 Non-vegetarisch recept"):
        resultaat = query_n8n("Geef me een recept met vlees of vis erin")
        st.session_state['last_response'] = resultaat

st.divider()

# --- VRIJE VRAGEN INPUT ---
user_input = st.chat_input("Stel je vraag over GA4 data of iets anders...")

if user_input:
    resultaat = query_n8n(user_input)
    st.session_state['last_response'] = resultaat

# --- RESULTAAT WEERGAVE ---
if 'last_response' in st.session_state:
    st.subheader("Antwoord van de Agent:")
    st.markdown(st.session_state['last_response'])
