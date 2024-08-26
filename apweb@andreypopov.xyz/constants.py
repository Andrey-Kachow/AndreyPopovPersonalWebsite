import os

class Paths:
    MAIN = os.path.dirname(os.path.abspath(__file__))
    DOCUMENTS_DIR = os.path.join(MAIN, 'static', 'documents')
    CV_PDF_PATH = os.path.join(DOCUMENTS_DIR, 'CV.pdf')    
    FRESHIFE_PDF_PATH = os.path.join(DOCUMENTS_DIR, 'freshlife_writeup.pdf')