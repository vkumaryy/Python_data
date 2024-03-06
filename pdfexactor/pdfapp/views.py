import json
from django.http import JsonResponse
from PyPDF2 import PdfReader
import re


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




# def extract_pdf_text(request):
#     """Extracts text data from a user-uploaded PDF file and returns it as a dictionary or JSON.

#     Args:
#         request (HttpRequest): The Django request object.

#     Returns:
#         JsonResponse: A JSON response containing the extracted text data or an error message.

#     Raises:
#         ValueError: If a PDF file is not uploaded or the file format is invalid.
#     """

#     if request.method != 'POST':
#         return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

#     try:
#         # Validate file upload
#         if 'pdf_file' not in request.FILES:
#             return JsonResponse({'error': 'No PDF file uploaded.'}, status=400)

#         pdf_file = request.FILES['pdf_file']

#         # Validate file extension
#         if not pdf_file.name.endswith('.pdf'):
#             return JsonResponse({'error': 'Invalid file format. Please provide a PDF file.'}, status=400)

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






# def extract_pdf_data(file_path: str) -> dict or None:
#     """Extracts Passenger Information, Baggage Information, and Fare Details from a local PDF file,
#     combining regular expressions and heuristic parsing.

#     Args:
#         file_path (str): The local file path to the PDF file.

#     Returns:
#         dict: A dictionary containing the extracted data or None if an error occurs.
#     """

#     try:
#         # Open the PDF using PyPDF2
#         with open(file_path, 'rb') as pdf_file:
#             reader = PdfReader(pdf_file)

#             # Extract text from all pages, combining them into a single string
#             text = ''
#             for page_num in range(len(reader.pages)):
#                 page = reader.pages[page_num]
#                 text += page.extract_text() + '\n'

#         # Combine text across multiple lines for better structure analysis
#         text_lines = [line.strip() for line in text.splitlines() if line.strip()]

#         # Define patterns for information extraction (modify as needed)
#         section_patterns = {
#             'passenger_info': r'Passenger Information|Passenger Details',
#             'baggage_info': r'Baggage Information|Checked Baggage',
#             'fare_details': r'Fare Details|Fare Summary|Your Fare',
#         }

#         extracted_data = {}

#         # Loop through text lines, grouping them based on information sections
#         current_section = None
#         section_data = []
#         for line in text_lines:
#             for section_name, pattern in section_patterns.items():
#                 if re.search(pattern, line, re.IGNORECASE):
#                     current_section = section_name
#                     section_data = []
#                     break  # Stop searching patterns after a match

#             if current_section:
#                 # Accumulate data within the current section
#                 section_data.append(line)

#             if current_section and not line:
#                 # End of section reached, process accumulated data
#                 if current_section == 'passenger_info':
#                     extracted_data['passenger_info'] = parse_passenger_info(section_data)
#                 elif current_section == 'baggage_info':
#                     extracted_data['baggage_info'] = parse_baggage_info(section_data)
#                 elif current_section == 'fare_details':
#                     # Replace this with your specific logic to parse fare details
#                     extracted_data['fare_details'] = parse_fare_details(section_data)

#                 current_section = None
#                 section_data = []

#         return extracted_data

#     except (IOError, FileNotFoundError) as e:
#         # Handle file-related errors with informative error message
#         error_message = f"Error reading PDF file: {str(e)}"
#         print(error_message)
#         return None  # Return None to indicate an error

#     except Exception as e:
#         # Catch unexpected errors and print the error message for logging or debugging
#         error_message = f"An unexpected error occurred: {str(e)}"
#         print(error_message)
#         return None  # Return None to indicate an error


# def parse_passenger_info(data_lines: list) -> dict or None:
#     """Parses data lines for Passenger Information.

#     Args:
#         data_lines (list): A list of text lines belonging to the Passenger Information section.

#     Returns:
#         dict: A dictionary containing extracted passenger information or None if parsing fails.
#     """

#     # Implement your specific logic to parse passenger information from `data_lines`.
#     # This is a placeholder example that assumes lines are in "key: value" format.
#     passenger_info = {}
#     for line in data_lines:
#         if ':' in line:
#             key, value = line.strip().split(':', 1)
#             passenger_info[key.strip()] = value.strip()
#     return passenger_info


# def parse_baggage_info(data_lines: list) -> dict or None:
#     """Parses data lines for Baggage Information.

#     Args:
#         data_lines (list): A list of text lines belonging to the Baggage Information section.

#     Returns:
#         dict: A dictionary containing extracted baggage information or None if parsing fails.
#     """
#     baggage_info = {}
#     for line in data_lines:
#         if 'Baggage' in line:
#             baggage_info['Baggage'] = line.strip()
#     return baggage_info
    




def extract_pdf_text(request):
    file_path = request.GET.get('file_path', '/home/vikash/Downloads/filght_ticket.pdf')

    try:
        if not file_path.endswith('.pdf'):
            raise ValueError('Invalid file format. Please provide a PDF file.')

        with open(file_path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)

            text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() + '\n'  # Add newlines between pages

        # Implement logic to search for and extract "Passenger Information" and "Baggage Information"
        passenger_info_start = text.find("Passenger Information")
        baggage_info_start = text.find("Baggage Information")

        passenger_info_end = baggage_info_start if baggage_info_start != -1 else None
        baggage_info_end = None  # Assume Baggage Information is the last section

        passenger_info_text = text[passenger_info_start:passenger_info_end].strip() if passenger_info_start != -1 else "Not Found"
        baggage_info_text = text[baggage_info_start:baggage_info_end].strip() if baggage_info_start != -1 else "Not Found"

        # Prepare data
        data = {
            'Passenger Information': passenger_info_text,
            'Baggage Information': baggage_info_text,
        }

        # Return JSON response
        return JsonResponse(data)

    except (IOError, FileNotFoundError) as e:
        return JsonResponse({'error': f"Error reading PDF file: {str(e)}"}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': f"An unexpected error occurred: {str(e)}"}, status=500)







