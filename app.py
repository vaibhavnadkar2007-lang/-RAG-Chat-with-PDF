import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.title("My RAG Project - Chat with PDF")
st.write("Upload PDF and ask questions!")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    st.success(f"PDF loaded! {len(chunks)} chunks created.")

    query = st.text_input("Ask question:")

    if query:
        # Fixed search
        query_lower = query.lower()
        found = []
        for c in chunks:
            if query_lower in c.lower():
                found.append(c)

        if found:
            st.write("**Answer:**")
            st.write(found[0])
        else:
            # if exact not found, search word by word
            words = query_lower.split()
            for c in chunks:
                for w in words:
                    if len(w) > 3 and w in c.lower():
                        found.append(c)
                        break
            if found:
                st.write("**Relevant Answer:**")
                st.write(found[0])
            else:
                st.write(chunks[0])