import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from the .env file.
# This keeps your API key secure and separate from the code.
load_dotenv()

# Initialize the Flask application.
app = Flask(__name__)

# --- Gemini API Configuration ---
# Retrieve the API key from the environment variable.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key is present. If not, raise an error to prevent the app from running.
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please add it.")

# Configure the generative AI library with your API key.
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini-Pro model for text generation.
model = genai.GenerativeModel('gemini-pro')

# --- Dummy Data for Disease Prediction ---
# In a real-world application, this data would come from a database
# or a machine learning model. This is for demonstration purposes.
symptoms = [
    "fever", "cough", "sore_throat", "headache", "nausea",
    "fatigue", "rash", "chills", "body_ache", "stomach_pain",
    "dizziness", "runny_nose", "sneezing", "vomiting"
]

disease_data = {
    "fever": {
        "description": "Fever is a temporary increase in your body temperature, often due to an illness.",
        "precautions": ["Rest well", "Drink plenty of fluids", "Take fever-reducing medication as prescribed"]
    },
    "cough": {
        "description": "A cough is a reflex action to clear your airways of irritants and mucus.",
        "precautions": ["Stay hydrated", "Use a humidifier", "Avoid irritants like smoke and dust"]
    },
    "headache": {
        "description": "A headache is a pain in any region of the head.",
        "precautions": ["Rest in a dark room", "Stay hydrated", "Use a cold compress"]
    },
    "rash": {
        "description": "A skin rash is an area of irritated or swollen skin that can be itchy.",
        "precautions": ["Avoid scratching the affected area", "Use a gentle, fragrance-free soap", "Apply a moisturizing lotion"]
    },
    # Add more diseases and their data as needed
}

# --- Flask Routes ---
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Handles the main page, displaying the symptom form and prediction results.
    """
    disease = None
    description = None
    precautions = []
    
    if request.method == "POST":
        selected_symptoms = request.form.getlist("symptoms")
        if selected_symptoms:
            # Simple prediction logic for demonstration: it predicts a disease
            # based on the first selected symptom.
            main_symptom = selected_symptoms[0]
            if main_symptom in disease_data:
                disease = main_symptom.replace("_", " ").title()
                description = disease_data[main_symptom]["description"]
                precautions = disease_data[main_symptom]["precautions"]

    return render_template("index.html", symptoms=symptoms, disease=disease, description=description, precautions=precautions)

@app.route("/chat", methods=["POST"])
def chat():
    """
    Handles chatbot messages by sending user input to the Gemini API
    and returning the generated response.
    """
    # Get the user's message from the JSON data sent by the frontend.
    data = request.json
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"response": "Please provide a message."}), 400

    try:
        # Generate content using the Gemini model.
        # This sends the user's message to the API.
        response = model.generate_content(user_message)
        bot_response = response.text
        return jsonify({"response": bot_response})
    except Exception as e:
        print(f"Error during Gemini API call: {e}")
        return jsonify({"response": "I'm sorry, I'm having trouble connecting right now. Please try again later."}), 500

# Run the Flask app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
