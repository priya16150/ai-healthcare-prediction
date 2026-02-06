from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# ======================
# Load datasets
# ======================
train = pd.read_csv(r"C:\ai_healthcare\Training.csv")
test = pd.read_csv(r"C:\ai_healthcare\Testing.csv")
desc = pd.read_csv(r"C:\ai_healthcare\disease_description.csv")
precaution = pd.read_csv(r"C:\ai_healthcare\disease_precaution.csv")

# Remove extra columns (if any)
train = train.loc[:, ~train.columns.str.contains('^Unnamed')]
test = test.loc[:, ~test.columns.str.contains('^Unnamed')]

# Prepare features
X_train = train.drop(columns=['prognosis'])
y_train = train['prognosis']

# Train ML model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# ======================
# Flask Routes
# ======================
@app.route("/", methods=["GET", "POST"])
def index():
    disease = None
    description = ""
    precautions = []

    if request.method == "POST":
        # Get selected symptoms
        selected_symptoms = request.form.getlist("symptoms")

        # Build patient feature vector
        new_patient = [0] * X_train.shape[1]
        for symptom in selected_symptoms:
            if symptom in X_train.columns:
                idx = X_train.columns.get_loc(symptom)
                new_patient[idx] = 1

        new_patient_df = pd.DataFrame([new_patient], columns=X_train.columns)

        # Predict disease
        prediction = model.predict(new_patient_df)
        disease = prediction[0]

        # Get description
        desc_row = desc[desc['Disease'] == disease]
        if not desc_row.empty:
            description = desc_row['Symptom_Description'].values[0]

        # Get precautions
        prec_row = precaution[precaution['Disease'] == disease]
        if not prec_row.empty:
            precautions = prec_row.iloc[0, 1:].dropna().tolist()

    # Send data to HTML
    return render_template(
        "index.html",
        symptoms=X_train.columns,
        disease=disease,
        description=description,
        precautions=precautions
    )

# ======================
# Run Flask App
# ======================
if __name__ == "__main__":
    app.run(debug=True)
