import streamlit as st
from langchain.docstore.document import Document
import os
from langchain.document_loaders import PyPDFLoader, CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import torch
from langchain.llms import huggingface_pipeline
import requests
from bs4 import BeautifulSoup
import bs4
import re
import tabulate
from github import Github
from load_models import load_embedding_model

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("Chat with PDFs using Generative AI")

with st.sidebar:
    st.subheader("Choose input type:")
    input_type = st.selectbox("Select the input source", 
                              ["PDF", "Q&A Dataset", "Website URL", "Code Snippets", "Documentation", "Github Code base URL"])

    if input_type == "PDF":
        pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
    elif input_type == "Q&A Dataset":
        qa_file = st.file_uploader("Upload a Q&A Dataset (CSV/JSON)", type=["csv", "json"])
    elif input_type == "Website URL":
        website_url = st.text_input("Enter the Website URL")
    elif input_type == "Code Snippets":
        code_snippets = st.text_area("Paste your code snippets here")
    elif input_type == "Documentation":
        documentation_file = st.file_uploader("Upload Documentation (PDF/TXT)", type=["pdf", "txt"])
    elif input_type == "Github Code base":
        github_url = st.text_input("Enter the Github Codebase URL")


def display_chat():
    for message in st.session_state["messages"]:
        st.write(f"{message['role']}: {message['content']}")

st.subheader("Chat History")
display_chat()

user_input = st.text_input("Enter your question or message:")

if st.button("Send"):
    if user_input:
        st.session_state["messages"].append({"role": "User", "content": user_input})
        st.experimental_rerun()

if input_type == "PDF" and pdf_file:
    st.write("You have uploaded a PDF.")
elif input_type == "Q&A Dataset" and qa_file:
    st.write("You have uploaded a Q&A dataset.")
elif input_type == "Website URL" and website_url:
    st.write(f"Website URL: {website_url}")
elif input_type == "Code Snippets" and code_snippets:
    st.write("You have entered code snippets.")
elif input_type == "Documentation" and documentation_file:
    st.write("You have uploaded documentation.")
elif input_type == "Github Code base" and github_url:
    st.write(f"Github Codebase URL: {github_url}")