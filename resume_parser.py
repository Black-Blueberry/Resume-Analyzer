import PyPDF2
import docx2txt
import io

def parse_resume(uploaded_file):
    file_type = uploaded_file.type

    if file_type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file format. Please upload a PDF or DOCX file."

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    text = docx2txt.process(io.BytesIO(file.read()))
    return text
