import json
import PyPDF2

import PyPDF2
import re

def extract_invoice_data(pdf_data):
    """
    Extracts specific data from a PDF using PyPDF2.

    Args:
        pdf_data (bytes): The byte content of the PDF file.

    Returns:
        dict (or None): A dictionary containing extracted invoice data or None if extraction fails.
    """

    try:
        # Open PDF in memory
        with io.BytesIO(pdf_data) as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)

        invoice_data = {}
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()

            # Use regular expressions to extract data points
            invoice_no_match = re.search(r'Tax invoice No:\s*(.*)', text, re.IGNORECASE)
            invoice_date_match = re.search(r'Invoice Date:\s*(.*)', text, re.IGNORECASE)
            client_name_match = re.search(r'Client name:\s*(.*)', text, re.IGNORECASE)
            total_tax_match = re.search(r'(Total Tax|Total tax|Tax Amount|Total due):\s*(\d+\.\d+)', text, re.IGNORECASE)

            if invoice_no_match:
                invoice_data['Tax invoice No'] = invoice_no_match.group(1)
            if invoice_date_match:
                invoice_data['Invoice Date'] = invoice_date_match.group(1)
            if client_name_match:
                invoice_data['Client name'] = client_name_match.group(1)
            if total_tax_match:
                invoice_data['Total tax amount'] = total_tax_match.group(2)

        return invoice_data

    except Exception as e:
        print(f"Error extracting data: {e}")
        return None


# Example usage
pdf_file_path = 'your_invoice.pdf'  # Replace with the actual path
extracted_data = extract_invoice_data(pdf_file_path)

if extracted_data:
    print("Extracted invoice data:")
    print(json.dumps(extracted_data, indent=4))  # Convert to JSON and print with indentation
else:
    print("Failed to extract data from the PDF.")
