import streamlit as st
from mistrilAPI import queryModel
import torch

st.title("Mistril Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
        query = [{"role": "user", "content": prompt},]
    st.session_state.messages.append(query[0])

    with st.chat_message("assistant"):
        response = queryModel(query)
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant", "content":response})


