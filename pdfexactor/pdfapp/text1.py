import io
import PyPDF2
import re

def extract_invoice_data(pdf_file_path, use_regex=False, regex_patterns=None):
    """
    Extracts specific data points from a given PDF file.

    Args:
        pdf_file_path (str): The path to the PDF file.
        use_regex (bool, optional): Use regular expressions for data extraction if True (default: False).
        regex_patterns (dict, optional): A dictionary containing regular expression patterns for specific data points.
            Keys should match the desired data field names (e.g., 'Tax invoice No', 'Invoice Date', etc.).
            Values should be the corresponding regular expression patterns.

    Returns:
        dict (or None): A dictionary containing extracted invoice data or None if extraction fails.
    """

    try:
        invoice_data = {}
        with open(pdf_file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()

                # Extract data using either PyPDF2 methods or regular expressions
                if not use_regex:
                    extracted_data = extract_using_py_pdf2(text)
                else:
                    if not regex_patterns:
                        raise ValueError("regex_patterns dictionary is required when use_regex is True")
                    extracted_data = extract_using_regex(text, regex_patterns)

                invoice_data.update(extracted_data)

                if invoice_data:
                    return invoice_data

        # No data found on all pages
        return None

    except Exception as e:
        print(f"Error extracting data: {e}")
        return None


def extract_using_py_pdf2(text):
    """
    Extracts data using PyPDF2 methods.

    Args:
        text (str): The extracted text content from a PDF page.

    Returns:
        dict: A dictionary containing extracted data points.
    """

    invoice_data = {}
    # Customize these patterns based on your actual PDF format
    invoice_no_match = re.search(r'Tax invoice No:', text, re.IGNORECASE)
    invoice_date_match = re.search(r'Invoice Date:', text, re.IGNORECASE)
    client_name_match = re.search(r'Client name:', text, re.IGNORECASE)
    total_tax_match = re.search(r'(Total Tax|Total tax|Tax Amount|Total due):', text, re.IGNORECASE)

    if invoice_no_match:
        invoice_data['Tax invoice No'] = text[invoice_no_match.end():].strip()
    if invoice_date_match:
        invoice_data['Invoice Date'] = text[invoice_date_match.end():].strip()
    if client_name_match:
        invoice_data['Client name'] = text[client_name_match.end():].strip()
    if total_tax_match:
        # Extract numeric portion, assuming a single tax amount
        total_tax_data = re.findall(r'\d+\.\d+', text[total_tax_match.end():])[0]
        invoice_data['Total tax amount'] = float(total_tax_data)

    return invoice_data


def extract_using_regex(text, regex_patterns):
    """
    Extracts data using provided regular expressions.

    Args:
        text (str): The extracted text content from a PDF page.
        regex_patterns (dict): A dictionary containing regular expression patterns for data points.

    Returns:
        dict: A dictionary containing extracted data points.
    """

    invoice_data = {}
    for field_name, pattern in regex_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted_value = match.group(1) if len(match.groups()) > 0 else match.group(0)
            invoice_data[field_name] = extracted_value

    return invoice_data


# Example usage
pdf_file_path = '/home/vikash/Downloads/filght_ticket.pdf'

# Define regex patterns for data extraction
regex_patterns = {
    'Tax invoice No': r'Tax invoice No:\s*(\w+)',
    'Invoice Date': r'Invoice Date:\s*(\d{2}/\d{2}/\d{4})',
    'Client Name': r'Client name:\s*(.+)',
    'Total Tax Amount': r'(Total Tax|Total tax|Tax Amount|Total due):\s*(\$\d+\.\d+)'
}

# Extract data using the function
extracted_invoice_data = extract_invoice_data(pdf_file_path, use_regex=True, regex_patterns=regex_patterns)
if extracted_invoice_data:
    print("Extracted Invoice Data:")
    for key, value in extracted_invoice_data.items():
        print(f"{key}: {value}")
else:
    print("No data extracted from the PDF.")
