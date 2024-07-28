from flask import Flask, render_template, request, url_for, redirect, flash
from processor import pdf_summarize, text_summarize, website_summarize

UPLOAD_FOLDER = "C:\\Users\\vivek\OneDrive\\Desktop\\Avik 2022\\Coding\\ai website summarization\\files"
 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == "GET":
		content = {"current-tab": "url"}
		return render_template('index.html', content=content)
	
	elif request.method == "POST":

		if 'url' in request.form.keys():
			url = request.form['url']
			content = website_summarize(url)

			return render_template('index.html', content=content)

		elif 'text' in request.form.keys():
			text = request.form['text']
			content = text_summarize(text)

			return render_template('index.html', content=content)
		elif 'pdf' in request.files:
			pdf = request.files['pdf']
			content = pdf_summarize(pdf)

			return render_template('index.html', content=content)
		
		else:
			return render_template('error.html')
		



 
# main driver function
if __name__ == '__main__':
	
	app.run(debug=True)