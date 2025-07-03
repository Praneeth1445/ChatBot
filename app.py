import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Configure Gemini API Key
GEMINI_API_KEY = "AIzaSyDs2W-2Hjw9qJ_8lLCwMcQFJz-gDbb8Hbo"

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app)

def generate_gemini_response(user_query):
    prompt = f"""
    You are an intelligent assistant. Given the user query, generate a helpful response. Response should be short and clear. Use emoji if needed. Conversations should be respectful.

    User Query: {user_query}

    Response:
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "No response from Gemini API."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        if not data or "query" not in data:
            return jsonify({"response": "Invalid request!"}), 400

        user_query = data["query"]
        print(f"Received query: {user_query}")

        final_response = generate_gemini_response(user_query)

        return jsonify({"response": final_response})

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"response": "Server error!"}), 500

if __name__ == "__main__":
    app.run(debug=True)
