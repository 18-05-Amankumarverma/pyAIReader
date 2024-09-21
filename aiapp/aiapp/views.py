from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PyPDF2 import PdfReader
import pyttsx3
from .forms import PDFUploadForm

def dashboard(request):
    form = PDFUploadForm()
    extracted_text = None
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            fs = FileSystemStorage()
            filename = fs.save(pdf_file.name, pdf_file)
            file_path = fs.path(filename)

            # Extract text from PDF
            extracted_text = extract_text_from_pdf(file_path)

            # Optionally, delete the file after extraction
            fs.delete(filename)

    return render(request, 'dashboard.html', {'form': form, 'extracted_text': extracted_text})

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def read_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            read_aloud(text)
    return render(request, 'dashboard.html')

def read_aloud(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def home(request):
    return render(request,'index.html')
