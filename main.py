import os
from pypdf import PdfReader
from tkinter import filedialog, Tk

def get_output_filename(pdf_path: str, metadata_title: str | None) -> str:
    """
    Determine a safe output filename:
    - Uses metadata_title if available
    - Falls back to the PDF’s filename otherwise
    - Strips out any invalid characters
    """
    if metadata_title:
        base = metadata_title
    else:
        base = os.path.splitext(os.path.basename(pdf_path))[0]
    # Allow only alphanumeric characters, spaces, hyphens, and underscores
    safe = "".join(c for c in base if c.isalnum() or c in (" ", "-", "_")).rstrip()
    return f"{safe}.txt"

def extract_all_text(pdf_path: str) -> tuple[str | None, str]:
    """
    Read the entire PDF and return:
      (metadata_title or None, the full extracted text)
    """
    reader = PdfReader(pdf_path)
    title = reader.metadata.title if reader.metadata else None
    text_parts: list[str] = []
    for page in reader.pages:
        # extract_text() may return None
        page_text = page.extract_text() or ""
        text_parts.append(page_text)
    full_text = "\n\n".join(text_parts)
    return title, full_text

def write_text_to_file(text: str, output_filename: str, output_dir: str = "output"):
    """
    Write the entire text into a single .txt file in the output directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, output_filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✔ Text successfully written to '{path}'.")

def select_pdf_file() -> str | None:
    """
    Open a file dialog to select a PDF file.
    """
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()
    filetypes = [("PDF files", "*.pdf"), ("All files", "*.*")]
    filename = filedialog.askopenfilename(title="Select a PDF", filetypes=filetypes)
    root.destroy()
    return filename if filename else None

if __name__ == "__main__":
    # 1) Prompt user to select a PDF
    pdf_path = select_pdf_file()
    if not pdf_path:
        print("⚠️ No file selected, aborting.")
        exit(1)

    # 2) Extract all text from the PDF
    metadata_title, full_text = extract_all_text(pdf_path)

    # 3) Determine the output filename
    output_filename = get_output_filename(pdf_path, metadata_title)

    # 4) Write the extracted text to the file
    write_text_to_file(full_text, output_filename)
