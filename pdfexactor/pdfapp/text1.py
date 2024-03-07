import io
import PyPDF2
import re


def extract_invoice_data(pdf_data, use_regex=False, regex_patterns=None):
    """
    Extracts specific data points from a given PDF byte stream.

    Args:
        pdf_data (bytes): The byte content of the PDF file.
        use_regex (bool, optional): Use regular expressions for data extraction if True (default: False).
        regex_patterns (dict, optional): A dictionary containing regular expression patterns for specific data points.
            Keys should match the desired data field names (e.g., 'Tax invoice No', 'Invoice Date', etc.).
            Values should be the corresponding regular expression patterns.

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


# Example usage
pdf_file_path = 'your_invoice.pdf'  # Replace with the actual path
extracted_data = extract_invoice_data(pdf_file_path)

if extracted_data:
    print("Extracted invoice data:")
    print(json.dumps(extracted_data, indent=4))  # Convert to JSON and print with indentation
else:
    print("Failed to extract data from the PDF.")



def extract_invoice_data(pdf_data, use_regex=False, regex_patterns=None):
    # ... (rest of the function)

# Example usage
pdf_file_path = 'your_invoice.pdf'
with open(pdf_file_path, 'rb') as pdf_file:  # Open in binary read mode
    pdf_data = pdf_file.read()

extracted_data = extract_invoice_data(pdf_data)
