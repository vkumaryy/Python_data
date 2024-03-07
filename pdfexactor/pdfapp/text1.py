import io
import PyPDF2
import re

def extract_invoice_data(pdf_file_path):
    try:
        invoice_data = {}
        with open(pdf_file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text = page.extract_text()
                extracted_data = extract_using_regex(text)
                invoice_data.update(extracted_data)
                if invoice_data:
                    return invoice_data
        return None
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def extract_using_regex(text):
    invoice_data = {}
    regex_patterns = {
        'Tax invoice No': r'Tax\s*invoice\s*No\s*:\s*(\w+)',
        'Invoice Date': r'Invoice\s*Date\s*:\s*(\d{2}/\d{2}/\d{4})',
        'Client Name': r'Client\s*Name\s*:\s*(.+)',
        'Total Tax Amount': r'Total\s*Tax\s*Amount\s*:\s*(\$\d+\.\d+)',
        'Total Tax': r'Total\s*Tax\s*:\s*(\$\d+\.\d+)'
    }
    for field_name, pattern in regex_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted_value = match.group(1).strip()
            invoice_data[field_name] = extracted_value
    return invoice_data

pdf_file_path = '/home/vikash/Downloads/filght_ticket.pdf'
extracted_invoice_data = extract_invoice_data(pdf_file_path)
if extracted_invoice_data:
    print("Extracted Invoice Data:")
    for key, value in extracted_invoice_data.items():
        print(f"{key}: {value}")
else:
    print("No data extracted from the PDF.")
