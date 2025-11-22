import streamlit as st
import tempfile
import asyncio
import os
from PDF_Reader import Read_From_PDF
from Agent import Agent_Run

st.title("PDF → Structured Data Extractor")
st.write("Upload a PDF and get a downloadable Output.xlsx")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

#Create a temporary file
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name

    st.success("PDF uploaded successfully. Processing...")

    #Using Read from pdf to extract text
    text = Read_From_PDF(temp_pdf_path)

    #run the main agent with the extracted text
    asyncio.run(Agent_Run(text))

    #path for download
    output_path = "output.xlsx"

    if os.path.exists(output_path):
        with open(output_path, "rb") as f:
            st.download_button(
                label="Download Output.xlsx",
                data=f,
                file_name="Output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        st.success("Click the button to download your Excel file.")
    else:
        st.error("Error: output.xlsx was not generated.")
