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
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages (using the updated method)
        num_pages = len(pdf_reader.pages)

        # Extract text from each page (modify as needed)
        text_data = {}
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text_data[f"Page {page_num + 1}"] = page.extractText()

        return text_data


