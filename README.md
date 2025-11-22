# PDF → Structured Excel Data Extractor

### This project extracts clean, structured data from any PDF file and converts it into a downloadable Output.xlsx file using an LLM-backed agent pipeline.

## Built with:

Python
Streamlit (frontend)
UV (package/environment manager)
LlamaIndex PDFReader
Microsoft Autogen Agents
OpenAI / Gemini LLm
Pandas for Excel output

## Structure

ASSESSMENT/
│
├── app.py                    -Streamlit frontend
├── Agent.py                  -LLM agent logic and Excel generator
├── PDF_Reader.py             -Reads PDF text using LlamaIndex
├── Prompt.py                 -All system messages
├── Main.py                   
├── Input_Path.py             -Not used in Streamlit but kept for reference
├── output.xlsx               -Generated file 
├── README.md                 -Full project documentation
├── pyproject.toml            -UV project file (dependencies, metadata)
├── requirements.txt          -Optional, for Streamlit deployment
├── .env                      -API keys (ignored in git)
├── .python-version           -Python version
└── .venv/                    -Virtual environment (ignored in git)


## Overview

### Agent.py :
This file has the main agent logic and outputs the .xlxs file

### PDF_Reader.py :
This file reads and extracts text from input pdf

### Main.py:
Orchestrates agent.py and PDF_Reader.py


# Run the project :

### pip install uv

### uv init      - Initialize the project 

### uv .venv     - Create virtual environment

- ### .venv/Scripts/Activate 

- ### for macos:  Source .venv/bin/activate

### uv pip install -r requirements.txt

### create .env file
- ### Add gemini api key via: GEMINI_API_KEY = "AIzaSyBxxxxxxxxx"

### streamlit run app.py


