from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Retrieve form data
        experience = int(request.form['experience'])
        test_score = int(request.form['test_score'])
        interview_score = int(request.form['interview_score'])

        # Create feature array
        final_features = np.array([[experience, test_score, interview_score]])

        # Predict salary
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template("index.html", prediction_text=f"Employee salary should be $ {output}")

    except Exception as e:
        return render_template("index.html", prediction_text="An error occurred: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
