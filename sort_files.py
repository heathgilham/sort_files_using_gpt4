import os
import openai
import fitz  # PyMuPDF
from docx import Document
import pytesseract
from PIL import Image
from dotenv import load_dotenv
import time

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(__file__))

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(file_path):
    try:
        text = ""
        with fitz.open(file_path) as doc:
            num_pages = min(3, len(doc))  # Process up to 3 pages or the total number of pages if fewer
            for page_num in range(num_pages):
                page = doc.load_page(page_num)  # Load each page
                page_text = page.get_text().strip()
                if not page_text:  # If no text, use OCR
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    page_text = pytesseract.image_to_string(img)
                text += page_text + '\n'  # Append text of each page with a newline
        return text.strip() if text else None
    except Exception as e:
        return f"Error: {e}"

def extract_text_from_docx(file_path):
    try:
        text = ""
        with open(file_path, 'rb') as f:
            doc = Document(f)
            for para in doc.paragraphs:
                text += para.text + '\n'
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        text += cell.text + ' \t'
                    text += '\n'
        return text.strip()
    except Exception as e:
        return f"Error: {e}"

def extract_text_from_file(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        return None

def is_about_toastmasters(text, file_path):
    if text:
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Is this text about First Aid? {text}"}],
                model="gpt-3.5-turbo"
            )
            response = chat_completion.choices[0].message.content

            return "yes" in response.lower()
        except Exception as e:
            print(f"Error in OpenAI API call for file {file_path}: {e}")
            return None
    else:
        return None

source_folder = 'input'
toastmasters_folder = 'toastmasters'
not_toastmasters_folder = 'not-toastmasters'

os.makedirs(source_folder, exist_ok=True)
os.makedirs(toastmasters_folder, exist_ok=True)
os.makedirs(not_toastmasters_folder, exist_ok=True)

for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.pdf') or file.endswith('.docx'):
            file_path = os.path.join(root, file)

            text = extract_text_from_file(file_path)

            result = is_about_toastmasters(text, file_path)
            if result is None:
                print(f"Skipping sorting of {file} due to API error.")
                continue
            
            # Add a delay before renaming
            time.sleep(1)

            if result:
                os.rename(file_path, os.path.join(toastmasters_folder, file))
                print(f"Moved {file} to toastmasters folder.")
            else:
                os.rename(file_path, os.path.join(not_toastmasters_folder, file))
                print(f"Moved {file} to not-toastmasters folder.")
