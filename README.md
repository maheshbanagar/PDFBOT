# PDFBOT
A chatbot that can extract and provide information from PDF documents. The chatbot will utilize the ChatGPT API to handle user queries and provide relevant responses based on the text extracted from the PDFs



## Implementation

- Create a virtual environment 

- Install necessary libraries
```bash
  pip install streamlit Image pytesseract pdf2image
```
- Download the tesseract using this [link](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe)

- set tesseract path (change this to the path on your system)
```bash
  pytesseract.pytesseract.tesseract_cmd = r'YOUR_TESSERACT_PATH'
```
- Get your chatGPT API key and replace with YOUR_API_TOKEN
```bash
headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_TOKEN",
        }
```
- Run the application
```bash
 python <fileName.py>
```

## Explanation
when user gives input as " /extract <pdf_path>" chatbot processes the document and extracts text. Now,User can input the queries related to the extracted information from the document
