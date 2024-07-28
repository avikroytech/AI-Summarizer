import os
import fitz

from openai import OpenAI
from web_scraping_test import get_main_content

API_SECRET_KEY = "SECRET KEY HERE"

client = OpenAI(api_key=API_SECRET_KEY)

websiteURL = "https://example.com"

def get_pdf_text(pdf_path):
	# Open the PDF file
	pdf_document = fitz.open(pdf_path)
	
	# Initialize an empty string to store the main text
	main_text = ""
	
	# Iterate through pages
	for page_number in range(pdf_document.page_count):
		# Get the page
		page = pdf_document[page_number]
		
		# Extract text from the page
		page_text = page.get_text()
		
		# Append the extracted text to the main text
		main_text += page_text
	
	# Close the PDF document
	pdf_document.close()

	# Delete the PDF file
	os.remove(pdf_path)

	# print(main_text)
	
	return main_text

# Example usage
# pdf_path = "C:\\Users\\vivek\\OneDrive\\Desktop\\Avik 2022\\Coding\\ai website summarization\\sample.pdf"
# main_text = get_pdf_text(pdf_path)
# print(main_text)

def get_website_summary(websiteURL):
	main_text = get_main_content(websiteURL)

	completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a professional literature scholar, who specializes in summarizing articles."},
			{"role": "user", "content": f"Please summarize this text. The summary should not be longer than one fourth words of the original text: {main_text}"}
		]
	)
	
	return completion.choices[0].message.content

def get_text_summary(text):
	
	completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a professional literature scholar, who specializes in summarizing articles."},
			{"role": "user", "content": f"Please summarize this text. The summary should not be longer than one fourth words of the original text: {text}"}
		]
	)

	return completion.choices[0].message.content

def get_pdf_summary(pdf_path):
	pdf_text = get_pdf_text(pdf_path)
	
	completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a professional literature scholar, who specializes in summarizing articles."},
			{"role": "user", "content": f"Please summarize this text. The summary should not be longer than one fourth words of the original text: {pdf_text}"}
		]
	)

	return completion.choices[0].message.content