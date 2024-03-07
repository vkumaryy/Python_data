import re
import pdfplumber

def extract_invoice_data(pdf_file_path):
    """
    Extracts specific data points using regular expressions from a PDF file.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        dict: A dictionary containing extracted invoice data.
    """
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            first_page = pdf.pages[0]  # Extract data from the first page

            # Extract text from the first page
            text = first_page.extract_text(x_tolerance=2, y_tolerance=2)

            # Regular expressions for data extraction
            tax_invoice_pattern = r'Tax\s*invoice\s*No\s*:\s*(\w+)'
            invoice_date_pattern = r'Invoice\s*Date\s*:\s*(\d{2}/\d{2}/\d{4})'
            total_tax_amount_pattern = r'Total\s*Tax\s*Amount\s*:\s*(\$\d+\.\d+)'
            total_tax_pattern = r'Total\s*Tax\s*:\s*(\$\d+\.\d+)'

            # Extracting data using regular expressions
            invoice_data = {}
            match_tax_invoice = re.search(tax_invoice_pattern, text, re.IGNORECASE)
            if match_tax_invoice:
                invoice_data['Tax invoice No'] = match_tax_invoice.group(1)

            match_invoice_date = re.search(invoice_date_pattern, text, re.IGNORECASE)
            if match_invoice_date:
                invoice_data['Invoice Date'] = match_invoice_date.group(1)

            match_total_tax_amount = re.search(total_tax_amount_pattern, text, re.IGNORECASE)
            if match_total_tax_amount:
                invoice_data['Total Tax Amount'] = match_total_tax_amount.group(1)

            match_total_tax = re.search(total_tax_pattern, text, re.IGNORECASE)
            if match_total_tax:
                invoice_data['Total Tax'] = match_total_tax.group(1)

            return invoice_data

    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# Example usage
pdf_file_path = 'your_invoice.pdf'
extracted_invoice_data = extract_invoice_data(pdf_file_path)
if extracted_invoice_data:
    print("Extracted Invoice Data:")
    print(extracted_invoice_data)
else:
    print("No data extracted from the PDF.")
