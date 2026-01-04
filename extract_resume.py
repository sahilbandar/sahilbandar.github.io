import sys
import os

pdf_path = "Resume_CG_Sahil_Updated_07-May-2025.pdf"

def extract_text():
    text = ""
    # Try pypdf
    try:
        from pypdf import PdfReader
        print("Using pypdf...")
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except ImportError:
        pass
    except Exception as e:
        print(f"pypdf failed: {e}")

    # Try PyPDF2
    try:
        import PyPDF2
        print("Using PyPDF2...")
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except ImportError:
        pass
    except Exception as e:
        print(f"PyPDF2 failed: {e}")

    # Try pdfplumber
    try:
        import pdfplumber
        print("Using pdfplumber...")
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    except ImportError:
        pass
    except Exception as e:
        print(f"pdfplumber failed: {e}")
        
    return None

extracted = extract_text()
if extracted:
    with open("resume_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted)
    print("Successfully wrote resume_text.txt")
else:
    print("No suitable PDF library found or extraction failed.")
