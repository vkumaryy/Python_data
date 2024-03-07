import pdfplumber
import json

def extract_invoice_data(pdf_file_path):
    """
    Extracts specific data points from a given PDF file.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        dict: A dictionary containing extracted invoice data or None if extraction fails.
    """

    try:
        invoice_data = {}
        with pdfplumber.open(pdf_file_path) as pdf:
            first_page = pdf.pages[0]  # Extract data from the first page

            # Extract text from the first page
            text = first_page.extract_text(x_tolerance=2, y_tolerance=2)

            # Extract data using text patterns
            invoice_data['Tax invoice No'] = text.split("Tax invoice No:")[-1].split("Invoice Date:")[0].strip()
            invoice_data['Invoice Date'] = text.split("Invoice Date:")[-1].split("Client Name:")[0].strip()
            invoice_data['Client Name'] = text.split("Client Name:")[-1].split("Total Tax Amount:")[0].strip()
            invoice_data['Total Tax Amount'] = text.split("Total Tax Amount:")[-1].split("Total Tax:")[0].strip()
            invoice_data['Total Tax'] = text.split("Total Tax:")[-1].strip()

            return invoice_data

    except Exception as e:
        print(f"Error extracting data: {e}")
        return None


# Example usage
pdf_file_path = '/home/vikash/Downloads/filght_ticket.pdf'
extracted_invoice_data = extract_invoice_data(pdf_file_path)
if extracted_invoice_data:
    print("Extracted Invoice Data:")
    print(json.dumps(extracted_invoice_data, indent=4))
else:
    print("No data extracted from the PDF.")
