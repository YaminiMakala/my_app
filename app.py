import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Digital Gujarat Chatbot!"

@app.route('/api/messages', methods=['POST'])
def bot_response():
    user_message = request.json.get('text', '')
    bot_reply = f"Hello! You said: {user_message}"
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    from waitress import serve
    port = int(os.environ.get('PORT', 8000))
    serve(app, host='0.0.0.0', port=port)

