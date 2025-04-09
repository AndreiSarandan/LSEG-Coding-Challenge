from flask import Flask, request, jsonify, render_template, session
from backend import calculate_response
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)


@app.route('/')
def home():
    return render_template('lseg-chat.html')


# Handle POST request from the chat
@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        user_request = request.get_json()
        user_selection = user_request.get("message", "")
        chat_response = calculate_response(user_selection, session)
        print(f"Chat response: {chat_response}") # Debug line
        return jsonify(chat_response)


# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)