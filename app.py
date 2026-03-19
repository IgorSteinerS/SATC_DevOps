import streamlit as st
import pandas as pd
from collections import Counter
import re


st.set_page_config(
    page_title="Analisador Rápido de texts",
    layout="centered"
)


def calculate_basic_metrics(text):
    chars_with_space = len(text)
    chars_without_space = len(text.replace(" ", ""))
    words = len(text.split())
    average_words_per_minute = 200
    reading_time = max(1, round(words / average_words_per_minute))

    return {
        "Caracteres (com espaços)": chars_with_space,
        "Caracteres (sem espaços)": chars_without_space,
        "Palavras": words,
        "Tempo de leitura (min)": reading_time,
    }


def extract_frequent_words(text, quantity=5):
    
    clean_text = re.sub(r"[^\w\s]", "", text.lower())
    words = clean_text.split()

    
    stopwords = {"de", "a", "o", "que", "e", "do", "da", "em", "um", "para",
                 "com", "uma", "os", "no", "se", "na", "por", "mais", "as",
                 "dos", "como", "mas", "ao", "ele", "das", "à", "seu", "sua",
                 "ou", "when", "the", "is", "in", "it", "of", "and", "to",
                 "a", "that", "was", "for", "on", "are", "with", "as", "at"}

    filtered_words = [p for p in words if p not in stopwords and len(p) > 2]

    contagem = Counter(filtered_words)
    most_comons = contagem.most_common(quantity)

    df = pd.DataFrame(most_comons, columns=["Palavra", "Frequência"])
    df.index += 1
    return df


# User interface with Streamlit
def main():
    st.title("Analisador Rápido de texts")
    st.write("Insira um bloco de text abaixo para extrair métricas instantâneas.")

    input_text = st.text_area(
        label="text para análise",
        placeholder="Cole seu text aqui...",
        height=250
    )

    if st.button("Analisar text"):
        if input_text.strip():
            metrics = calculate_basic_metrics(input_text)
            dataframe_frequents = extract_frequent_words(input_text)

            st.subheader("Métricas Gerais")
            cols = st.columns(4)
            for col, (label, valor) in zip(cols, metrics.items()):
                col.metric(label=label, value=valor)

            st.subheader("Palavras Mais Frequentes")
            st.dataframe(dataframe_frequents, use_container_width=True)
        else:
            st.warning("Por favor, insira algum text antes de analisar.")


if __name__ == "__main__":
    main()