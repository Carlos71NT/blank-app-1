import streamlit as st


st.title("Minha Rede de Segurança")

nome = st.text_input("Digite seu NOME:")
st.write("Você digitou:",nome)

senha = st.number_input("Digite sua SENHA:", min_value=0, max_value=999)
st.write("senha:",senha)

aceita = st.checkbox("Aceito os termos")
if aceita:
    st.write("Obrigado!")

if st.button("ENVIAR"):
    st.write("Enviado com sucesso")

    
import pandas as pd

