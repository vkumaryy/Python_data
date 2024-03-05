import os
import subprocess
from PyPDF2 import PdfReader

def extract_text_to_notepad(folder_path):
  """
  Extracts text from all PDFs in a folder and displays them in notepad.

  Args:
      folder_path: Path to the folder containing the PDFs.
  """
  text_data = {}
  for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
      file_path = os.path.join(folder_path, filename)
      try:
        with open(file_path, 'rb') as f:
          reader = PdfReader(f)
          text = ""
          for page in reader.pages:
            text += page.extract_text()
          text_data[filename] = text
      except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
      except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

  # Use notepad++ to display the dictionary content. You can adjust this line.
  subprocess.run(["notepad++", str(text_data)])

# Example usage
folder_path = "/path/to/your/folder"
extract_text_to_notepad(folder_path)
