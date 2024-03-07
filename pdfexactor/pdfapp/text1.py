import PyPDF2
import re

def extract_data_from_pdf(pdf_file_path):
    tax_invoice_no_pattern = r'Tax Invoice No:\s*(\w+)'
    invoice_date_pattern = r'Invoice Date:\s*(\d{2}/\d{2}/\d{4})'
    client_name_pattern = r'Client Name:\s*(.+)'
    total_tax_amount_pattern = r'Total Tax Amount:\s*(\$\d+\.\d+)'
    total_tax_pattern = r'Total Tax:\s*(\$\d+\.\d+)'
    
    extracted_data = {
        "Tax Invoice No": None,
        "Invoice Date": None,
        "Client Name": None,
        "Total Tax Amount": None,
        "Total Tax": None
    }
    
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text = page.extractText()
            
            match_tax_invoice_no = re.search(tax_invoice_no_pattern, text)
            if match_tax_invoice_no:
                extracted_data["Tax Invoice No"] = match_tax_invoice_no.group(1)
            
            match_invoice_date = re.search(invoice_date_pattern, text)
            if match_invoice_date:
                extracted_data["Invoice Date"] = match_invoice_date.group(1)
            
            match_client_name = re.search(client_name_pattern, text)
            if match_client_name:
                extracted_data["Client Name"] = match_client_name.group(1)
            
            match_total_tax_amount = re.search(total_tax_amount_pattern, text)
            if match_total_tax_amount:
                extracted_data["Total Tax Amount"] = match_total_tax_amount.group(1)
            
            match_total_tax = re.search(total_tax_pattern, text)
            if match_total_tax:
                extracted_data["Total Tax"] = match_total_tax.group(1)
    
    return extracted_data

# Example usage
pdf_file_path = 'example.pdf'
extracted_data = extract_data_from_pdf(pdf_file_path)
print(extracted_data)
