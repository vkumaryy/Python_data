from django.http import HttpResponse
from django.shortcuts import render
import PyPDF2
import subprocess

def extract_text_and_show_in_notepad(request):
    try:
        pdf_path = "path/to/your/pdf_file.pdf"  # Update with your PDF file path
        text_data = extract_text_from_pdf(pdf_path)
        
        # Show the text data in Notepad
        with open("temp_text_data.txt", "w", encoding="utf-8") as temp_file:
            for page, text in text_data.items():
                temp_file.write(f"=== {page} ===\n{text}\n\n")
        
        # Open Notepad with the text data file
        subprocess.Popen(["notepad.exe", "temp_text_data.txt"])

        return HttpResponse("Text extracted and displayed in Notepad.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")

def extract_text_from_pdf(pdf_path):
  # Open the PDF file
  with open(pdf_path, 'rb') as file:
    # Create a PDF reader object using PdfReader
    pdf_reader = PyPDF2.PdfReader(file)
  
    # Initialize an empty dictionary to store text data
    text_data = {}
  
    # Iterate through each page of the PDF
    for page_num in range(pdf_reader.getNumPages()):
      # Get the page object
      page = pdf_reader.getPage(page_num)
  
      # Extract text from the page
      text_data[f"Page {page_num + 1}"] = page.extractText()
  
    return text_data

