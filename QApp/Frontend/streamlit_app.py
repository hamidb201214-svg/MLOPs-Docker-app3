# QApp/Frontend/streamlit_app.py
import streamlit as st
from QApp.Backend.qa_service import answer_question
import sys

sys.path.insert(0, 'workspace/MLOPs-Docker-app3')
 
st.title("QApp - Simple Docker Demo")
question = st.text_input("Ask a question")
 
if st.button("Ask") and question.strip():
    st.success(answer_question(question))
