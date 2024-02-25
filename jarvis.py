import pathlib
import textwrap

import google.generativeai as genai




def jarvis(api_key,input):
  
	model = genai.GenerativeModel('gemini-pro')

	genai.configure(api_key=api_key)
	response = model.generate_content(input)
	print(response.text)
	return response.text





