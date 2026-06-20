import streamlit as st
from dotenv import load_dotenv


def main():
  load_dotenv()
  st.set_page_config(page_title ="Chat with multiple PDFs", page_icon="📚")
  
  st.header("Chat with multiple PDFs : 📚")
  st.text_input("Ask a question about your document:")

  with st.sidebar:
     st.subheader("Your document")
     pdf_docs = st.file_uploader(
        "Upload your PDFs here and click on Process", accept_multiple_files=True)
     if st.button("Process"):
       with st.spinner("Processing"):
       # get pdf text
        raw_text = get_pdf_text(pdf_docs)


if __name__ == '__main__':
    main()