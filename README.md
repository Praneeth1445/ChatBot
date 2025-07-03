<<<<<<< HEAD
# Gemini Chatbot

This project is a simple web-based AI chatbot that uses Google's Gemini Generative AI API to generate intelligent responses to user queries. The backend is built with Flask, and the frontend is provided as HTML files for user interaction.

## Features
- Conversational AI chatbot powered by Gemini API
- Modern, responsive web UI (see `index.html` and `bott.html`)
- REST API endpoint for chat interaction
- CORS enabled for frontend-backend communication

## Project Structure
- `app.py` / `bot.py`: Flask backend serving the chat API and connecting to Gemini
- `index.html`, `bott.html`: Frontend web UIs for chatting with the bot

## Requirements
See `requirements.txt` for Python dependencies.

## Setup & Usage

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your Gemini API key**
   - The API key is hardcoded in the Python files as `GEMINI_API_KEY`. For production, set it as an environment variable and update the code to read from the environment.

3. **Run the backend**
   ```bash
   python app.py
   # or
   python bot.py
   ```
   The server will start at `http://127.0.0.1:5000`.

4. **Open the frontend**
   - Open `index.html` or `bott.html` in your browser.
   - Type your message and interact with the chatbot!

## API
- **POST** `/chat`
  - Request JSON: `{ "query": "Your message here" }`
  - Response JSON: `{ "response": "AI's reply" }`

## Notes
- Requires a valid Gemini API key from Google.
- For local testing, CORS is enabled.
- The UI is static and does not require a web server; just open the HTML file in your browser.

## License
This project is for educational/demo purposes only. 
=======
# ChatBot
>>>>>>> 5104a5355acb0689ef4cf19a78bc1e8863f9bb4c
