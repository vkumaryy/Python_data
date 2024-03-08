import json
import re

from django.http import JsonResponse

def extract_pdf_data(request):
    """
    API view to extract tax invoice number from a raw PDF text string in a POST request.

    **Expected request format (POST):**

    ```json
    {
        "pdf_text": (str, required)
    }
    ```

    **Returns:**

    A JSON response containing the extracted tax invoice number and label, or an empty string if not found:

    ```json
    {
        "Tax Invoice No": "81315002" (or an empty string if not found)
    }
    ```
    """

    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    if 'pdf_text' not in request.POST:
        return JsonResponse({'error': 'Missing pdf_text field in request body'}, status=400)

    pdf_text = request.POST['pdf_text']

    # Enhanced regular expression for flexibility (same as previous version)
    tax_invoice_pattern = r"""
        (?:
            Tax\s+Invoice\s+No\.|  # Tax Invoice No. (with optional space)
            Tax\s+Invoice\s*[:],    # Tax Invoice: (with optional space and comma)
            Invoice\s+No\.|          # Invoice No.
            Invoice\s*[:]            # Invoice: (with optional space and colon)
        )\s*
        (\w+\s*\d+)              # Capture alphanumeric + digits (including spaces)
    """

    match = re.search(tax_invoice_pattern, pdf_text, re.IGNORECASE | re.VERBOSE)  # Verbose flag for readability

    if match:
        tax_invoice_no = match.group(2).strip()  # Extract only the number (group 2)
        data = {"Tax Invoice No": tax_invoice_no}  # Create dictionary with label and value
    else:
        data = {}  # Empty dictionary if not found

    return JsonResponse(data)
