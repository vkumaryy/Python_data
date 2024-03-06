import json
from django.http import JsonResponse
from PyPDF2 import PdfReader


# def extract_pdf_text(request, file_path: str = '/home/vikash/Downloads/filght_ticket.pdf'):
#     """Extracts text data from a local PDF file and returns it as a dictionary or JSON.

#     Args:
#         request (HttpRequest): The Django request object.
#         file_path (str): The local file path to the PDF file.

#     Returns:
#         JsonResponse: A JSON response containing the extracted text data.

#     Raises:
#         ValueError: If the provided file path is not a PDF file.
#     """

#     try:
#         # Validate file extension
#         if not file_path.endswith('.pdf'):
#             raise ValueError('Invalid file format. Please provide a PDF file.')

#         # Open the PDF using PyPDF2
#         with open(file_path, 'rb') as pdf_file:
#             reader = PdfReader(pdf_file)

#             # Extract text from all pages, combining them into a single string
#             text = ''
#             for page_num in range(len(reader.pages)):
#                 page = reader.pages[page_num]
#                 text += page.extract_text() + '\n'  # Add newlines between pages

#             # Prepare dictionary and JSON data
#             data = {'text': text.strip()}
#             json_data = json.dumps(data, indent=4)

#         # Return JSON response
#         return JsonResponse(json_data, safe=False)

#     except (IOError, FileNotFoundError) as e:
#         # Handle file-related errors
#         error_message = f"Error reading PDF file: {str(e)}"
#         return JsonResponse({'error': error_message}, status=400)

#     except ValueError as e:
#         # Handle invalid file format error
#         return JsonResponse({'error': str(e)}, status=400)

#     except Exception as e:
#         # Catch unexpected errors
#         error_message = f"An unexpected error occurred: {str(e)}"
#         return JsonResponse({'error': error_message}, status=500)




# def extract_pdf_text(request):
#     """Extracts text data from a user-uploaded PDF file and returns it as a dictionary or JSON.

#     Args:
#         request (HttpRequest): The Django request object.

#     Returns:
#         JsonResponse: A JSON response containing the extracted text data.

#     Raises:
#         ValueError: If a PDF file is not uploaded or the file format is invalid.
#     """

#     if request.method != 'POST':
#         return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

#     try:
#         # Validate file upload
#         if 'pdf_file' not in request.FILES:
#             raise ValueError('No PDF file uploaded. Please select a PDF file.')

#         pdf_file = request.FILES['pdf_file']

#         # Validate file extension
#         if not pdf_file.name.endswith('.pdf'):
#             raise ValueError('Invalid file format. Please provide a PDF file.')

#         # Extract file path
#         file_path = pdf_file.name  # Get the file name from the uploaded file

#         # Rest of the function logic to extract and return text data (unchanged)
#         # ...

#     except (IOError, FileNotFoundError) as e:
#         # Handle file-related errors
#         error_message = f"Error reading PDF file: {str(e)}"
#         return JsonResponse({'error': error_message}, status=400)

#     except ValueError as e:
#         # Handle invalid file format or missing upload error
#         return JsonResponse({'error': str(e)}, status=400)

#     except Exception as e:
#         # Catch unexpected errors
#         error_message = f"An unexpected error occurred: {str(e)}"
#         return JsonResponse({'error': error_message}, status=500)




# def extract_pdf_text(request):
#     """Extracts text data from a PDF file uploaded by the user and returns it as JSON.

#     Args:
#         request (HttpRequest): The Django request object.

#     Returns:
#         JsonResponse: A JSON response containing the extracted text data.

#     Raises:
#         ValueError: If no PDF file is uploaded or the file format is invalid.
#     """

#     if request.method != 'POST':
#         return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

#     try:
#         # Validate file upload
#         if 'pdf_file' not in request.FILES:
#             raise ValueError('No PDF file uploaded. Please select a PDF file.')

#         pdf_file = request.FILES['pdf_file']

#         # Validate file extension
#         if not pdf_file.name.endswith('.pdf'):
#             raise ValueError('Invalid file format. Please provide a PDF file.')

#         # Extract text from file
#         with open(pdf_file.temporary_name(), 'rb') as f:
#             reader = PdfReader(f)
#             text = ''
#             for page_num in range(len(reader.pages)):
#                 page = reader.pages[page_num]
#                 text += page.extract_text() + '\n'  # Add newlines between pages

#         # Prepare and return JSON data
#         data = {'text': text.strip()}
#         json_data = json.dumps(data, indent=4)  # Use indentation for readability

#         return JsonResponse(json_data, safe=False)

#     except (IOError, FileNotFoundError) as e:
#         # Handle file-related errors
#         error_message = f"Error reading PDF file: {str(e)}"
#         return JsonResponse({'error': error_message}, status=400)

#     except ValueError as e:
#         # Handle invalid file format or missing upload error
#         return JsonResponse({'error': str(e)}, status=400)

#     except Exception as e:
#         # Catch unexpected errors
#         error_message = f"An unexpected error occurred: {str(e)}"
#         return JsonResponse({'error': error_message}, status=500)




def extract_pdf_text(request):
    """Extracts text data from a user-uploaded PDF file and returns it as a dictionary or JSON.

    Args:
        request (HttpRequest): The Django request object.

    Returns:
        JsonResponse: A JSON response containing the extracted text data or an error message.

    Raises:
        ValueError: If a PDF file is not uploaded or the file format is invalid.
    """

    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

    try:
        # Validate file upload
        if 'pdf_file' not in request.FILES:
            return JsonResponse({'error': 'No PDF file uploaded.'}, status=400)

        pdf_file = request.FILES['pdf_file']

        # Validate file extension
        if not pdf_file.name.endswith('.pdf'):
            return JsonResponse({'error': 'Invalid file format. Please provide a PDF file.'}, status=400)

        # Extract text from file
        with open(pdf_file.temporary_name(), 'rb') as f:
            reader = PdfReader(f)
            text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() + '\n'  # Add newlines between pages

        # Prepare and return JSON data
        data = {'text': text.strip()}
        json_data = json.dumps(data, indent=4)  # Use indentation for readability

        return JsonResponse(json_data, safe=False)

    except (IOError, FileNotFoundError) as e:
        # Handle file-related errors
        error_message = f"Error reading PDF file: {str(e)}"
        return JsonResponse({'error': error_message}, status=400)

    except ValueError as e:
        # Handle invalid file format or missing upload error
        return JsonResponse({'error': str(e)}, status=400)

    except Exception as e:
        # Catch unexpected errors
        error_message = f"An unexpected error occurred: {str(e)}"
        return JsonResponse({'error': error_message}, status=500)




