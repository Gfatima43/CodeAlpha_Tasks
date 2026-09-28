from flask import Flask, jsonify, render_template, request
from chatbot import chatbot_response

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/chat")
def chat():
    data = request.get_json(silent=True)
    message = data.get("message") if isinstance(data, dict) else None
    
    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Message cannot be empty."}), 400
    return jsonify({"response": chatbot_response(message)})

if __name__ == "__main__":
    app.run(debug=True, port=5001)