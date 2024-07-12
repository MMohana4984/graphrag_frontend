import fitz 
import os

def pdf_to_text(pdf_path, txt_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    
    # Iterate over each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    # Save the text to a file
    with open(txt_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

def convert_pdfs_to_text(pdf_folder, txt_folder):
    # Create the input folder if it doesn't exist
    if not os.path.exists(txt_folder):
        os.makedirs(txt_folder)
    
    # Iterate over each PDF in the folder
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            txt_file = os.path.splitext(pdf_file)[0] + ".txt"
            txt_path = os.path.join(txt_folder, txt_file)
            pdf_to_text(pdf_path, txt_path)
            print(f"Converted {pdf_file} to {txt_file}")

# Define the folder paths
pdf_folder = "pdfs"
txt_folder = "input"

# Convert all PDFs in the folder
convert_pdfs_to_text(pdf_folder, txt_folder)
