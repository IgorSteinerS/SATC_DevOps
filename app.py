import streamlit as st
import pandas as pd
from collections import Counter
import re


st.set_page_config(
    page_title="Analisador Rápido de Textos",
    layout="centered"
)


def calcular_metricas_basicas(texto):
    """
    Deve retornar o número de caracteres (com e sem espaços),
    número de palavras e tempo estimado de leitura.
    """
    pass

def extrair_palavras_frequentes(texto, quantidade=5):
    """
    Deve limpar o texto, contar as palavras e retornar
    um DataFrame do Pandas com as 'n' mais frequentes.
    """
    pass

# Interface do Usuário (UI)
def main():
    st.title("Analisador Rápido de Textos")
    st.write("Insira um bloco de texto abaixo para extrair métricas instantâneas.")

    
    texto_entrada = st.text_area(
        label="Texto para análise",
        placeholder="Cole seu texto aqui...",
        height=250
    )

    
    if st.button("Analisar Texto"):
        if texto_entrada.strip():
            
            st.info("Processamento será implementado aqui.")
        else:
            st.warning("Por favor, insira algum texto antes de analisar.")

if __name__ == "__main__":
    main()