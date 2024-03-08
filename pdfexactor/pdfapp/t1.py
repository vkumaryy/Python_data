import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pdfminer.high_level import extract_text

@csrf_exempt
def extract_pdf_data(request):
    """
    API view to extract tax invoice number from a PDF uploaded in a POST request.
    """

    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    if 'pdf_file' not in request.FILES:
        return JsonResponse({'error': 'Missing pdf_file field in request body'}, status=400)

    pdf_file = request.FILES['pdf_file']

    try:
        # Using pdfminer.six to extract text from the entire PDF
        text = extract_text(pdf_file)

        tax_invoice_pattern = r"""
            (?:Tax\s+Invoice\s+No\.|    # Different possible prefixes
            Tax\s+Invoice[:]|           # for the invoice number
            Invoice\s+No\.|
            Invoice[:])\s*
            ([\w\s]+)                    # The actual invoice number pattern
        """
        match = re.search(tax_invoice_pattern, text, re.IGNORECASE | re.VERBOSE)

        if match:
            tax_invoice_no = match.group(1).strip()  # Extract the invoice number
        else:
            tax_invoice_no = ""  # No match found

        return JsonResponse({'tax_invoice_no': tax_invoice_no})

    except Exception as e:
        return JsonResponse({'error': f'Error processing PDF: {str(e)}'}, status=500)

