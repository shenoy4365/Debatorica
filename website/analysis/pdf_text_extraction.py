import PyPDF2
import language_tool_python
import re
from io import BytesIO

def extract_text_from_pdf(file_bytes: BytesIO):
    """Extract text from an in-memory PDF file and correct grammar mistakes."""
    text = ""

    # Read the file in memory
    file_bytes.seek(0)  # Reset the file pointer to the beginning
    pdf_reader = PyPDF2.PdfReader(file_bytes)

    # Iterate through the pages and extract text
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # Remove links using regex
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Initialize the language tool
    tool = language_tool_python.LanguageTool('en-US')

    # Check for grammar issues
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)

    return corrected_text

# Example usage:
# with open('your_pdf_file.pdf', 'rb') as file:
#     file_bytes = BytesIO(file.read())
#     extracted_text = extract_text_from_pdf(file_bytes)
#     print(extracted_text)
