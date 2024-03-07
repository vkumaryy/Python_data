import json
import PyPDF2
from camelot import Table

def extract_invoice_data(pdf_file_path):
    """
    Extracts invoice data from a given PDF file using Camelot.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        dict (or None): A dictionary containing extracted invoice data or None if extraction fails.
    """

    try:
        # Open PDF and build Camelot tables
        with open(pdf_file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            tables = Table(pages=reader.pages)

        # Extract specific data from the first table (assuming relevant data is in the first table)
        invoice_data = {}
        if len(tables) > 0:
            data = tables[0].df
            invoice_data['Tax invoice No'] = data.loc[data['Tax invoice No'].notna(), 'Tax invoice No'].tolist()[0]
            invoice_data['Invoice Date'] = data.loc[data['Invoice Date'].notna(), 'Invoice Date'].tolist()[0]
            invoice_data['Client name'] = data.loc[data['Client name'].notna(), 'Client name'].tolist()[0]
            for col in data.columns:
                if 'Total Tax' in col:
                    invoice_data['Total tax amount'] = data[col].tolist()[0]
                    break

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
