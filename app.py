import streamlit as st
from openai import OpenAI

# 🔑 Configuration OpenAI API Key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Charger la FAQ
with open("faq.txt", "r", encoding="utf-8") as f:
    faq_content = f.read()

# Interface utilisateur
st.title("🤖 Chatbot FAQ")
st.write("Posez vos questions, je réponds à partir de la FAQ de l'entreprise.")

question = st.text_input("Votre question :")

if question:
    prompt = f"Réponds de manière claire et concise à la question suivante en te basant uniquement sur ces informations :\n\n{faq_content}\n\nQuestion: {question}\nRéponse:"
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write("💬 Réponse :", response.choices[0].message.content)
