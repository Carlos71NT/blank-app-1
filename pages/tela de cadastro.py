import streamlit as st


st.title("Minha Rede de Segurança")

nome = st.text_input("Digite seu NOME:")
st.write("Você digitou:",nome)

email = st.text_input("Digite seu EMAIL:")
st.write("Você digitou:",email)

cpf = st.number_input("Digite seu CPF:", min_value=00000000000, max_value=99999999999)
st.write("Você digitou:",cpf)

senha = st.number_input("Digite sua SENHA:", min_value=0, max_value=999)
st.write("senha:",senha)

senha2 = st.number_input("CONFIRME SUA SENHA:", min_value=0, max_value=999)
st.write("senha2:",senha2)


aceita = st.checkbox("Aceito os termos")
if aceita:
    st.write("Obrigado!")

if st.button("ENVIAR"):
    st.write("Enviado com sucesso")

    
import pandas as pd

