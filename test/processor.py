import os
import validators

from openai_test import get_text_summary, get_website_summary, get_pdf_summary
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = ['pdf']
UPLOAD_FOLDER = "../files"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def website_summarize(url):
	validation = validators.url(url)

	if validation:
		summary = get_website_summary(url)

		response = {"current-tab": "url", "summary": summary, "url": url, "type": "url"}
		
		return response
	else:
		response = {
			"current-tab": "url",
			"url": url,
			"url-error": True
		}
		return response

def text_summarize(text):
	if len(text) > 300:
		summary = get_text_summary(text)

		response = {
			"current-tab": "text", 
			"summary": summary, 
			"type": "text", 
			"text": text
		}
		
		return response
	else:
		response = {
			"current-tab": "text",
			"text": text,
			"text-error": True
		}
		return response
	
def pdf_summarize(pdf):
	if pdf.filename == '':
		response = {
			"current-tab": "pdf",
			"pdf-error": True
		}
		return response
	if pdf and allowed_file(pdf.filename):
		pdfname = secure_filename(pdf.filename)
		pdf_path = os.path.join(UPLOAD_FOLDER, pdfname)
		pdf.save(pdf_path)

		summary = get_pdf_summary(pdf_path)

		response = {
			"current-tab": "pdf",
			"summary": summary,
			"type": "pdf",
			"pdf": pdf
		}

		return response
	
	response = {
			"current-tab": "pdf",
			"pdf-error": True
		}
	return response


