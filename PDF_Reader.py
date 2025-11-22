from llama_index.readers.file import PDFReader #can use any pdf reader

#reading and converting into string
def Read_From_PDF(path:str):
    reader = PDFReader()
    docs = reader.load_data(path) #read
    text = "".join(data.text.replace("\n","") for data in docs if getattr(data,"text",None)) #extracted text
    print("Text Extracted From PDF Successfully")
    return text