import streamlit as st 

st.title("Halloween Movie Recommender")
scare_level = st.slider("Scare Level", 0, 10)
print(scare_level)