I solved this challenge using a Python framework which I was already familiar with, Flask. This is a simple yet powerful backend development tool, perfectly suitable for creating a web-based chat bot. In order to ensure a smooth communication between Server and Client I used asynchronous JavaScript functions.

While this is a relatively short and simple project, I followed the default Flask file structure:
	-> store HTML files in templates folder
	-> store JS + CSS in static folder
	-> configure API endpoints for HTTP requests in main.py
	-> chat bot logic (parsing the .json file) implemented in backend.py 


Start application:
1. Install dependencies listed in requirements.txt: -> pip install -r requirements.txt
2. Run main.py 
	-> this starts the Flask server on local host
3. Access the chat bot on http://127.0.0.1:5000/ in web browser