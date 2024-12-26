import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    text = 'Why hello there'
    st.write(text)

if st.button('clear'):
    text = 'Goodbye'
    st.write(text)

