# 🩺 AI Healthcare Disease Prediction & Chatbot (Flask)

This project is a **Flask-based healthcare web application** that:
1. Predicts diseases based on selected symptoms using a **Decision Tree ML model**
2. Displays **disease description and precautions** from CSV datasets
3. Includes an **AI-powered chatbot** using **Google Gemini (Generative AI)** for health-related suggestions

No magic. No hype. Just a clean end-to-end mini healthcare system.

---

## 🚀 Features

- ✅ Symptom-based disease prediction
- ✅ Machine Learning with `scikit-learn`
- ✅ Pandas-based CSV data handling
- ✅ Clean Bootstrap-based UI
- ✅ Gemini-powered AI chatbot
- ✅ Secure API key handling using `.env`

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Bootstrap 5, JavaScript
- **ML Model:** Decision Tree Classifier (scikit-learn)
- **AI Chatbot:** Google Gemini (google-generativeai)
- **Data Handling:** Pandas

---

## 📁 Project Structure

```
ai_healthcare/
│
├── app.py                 # Flask backend (ML + Gemini chatbot)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── Training.csv           # ML training dataset
├── Testing.csv            # ML testing dataset
├── disease_description.csv
├── disease_precaution.csv
│
├── templates/
│   └── index.html         # Main UI
│
└── README.md
```

---

## 📦 Requirements

`requirements.txt`

```
Flask
pandas
scikit-learn
python-dotenv
google-generativeai
```

Install dependencies:

```bash
pip install -r requirements.txt
## ▶️ How to Run the Project

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

## 🧠 How Disease Prediction Works

- Symptoms are selected via checkboxes
- A binary feature vector is created
- A **DecisionTreeClassifier** predicts the disease
- Disease description & precautions are fetched from CSV files

This is **rule-based ML**, not deep learning. Simple, fast, explainable.

---

## 🤖 Chatbot Logic

- User message → `/chat` API
- Message sent to **Gemini-Pro model**
- AI-generated response returned as JSON

This chatbot is **advisory**, not diagnostic.

---

## ⚠️ Disclaimer

This application is **for educational purposes only**.

❌ Not a medical diagnosis system
❌ Not a replacement for doctors

Always consult qualified medical professionals.

---

## 💡 Possible Improvements (Real Talk)

- Replace CSVs with a database
- Add symptom severity & duration
- Improve ML model (RandomForest / XGBoost)
- Add user authentication
- Deploy using Docker + Gunicorn

---

## 👤 Author

Built for learning Flask, ML integration, and Gemini API usage.

If this breaks — fix the data first, not the model 😄

---

## 📜 License

Free to use for learning and academic projects.
