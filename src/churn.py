from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

df_1 = pd.read_csv("churn.csv")
model = pickle.load(open("model.sav", "rb"))
model_columns = pickle.load(open("columns.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        try:
            data = {
                "SeniorCitizen": int(request.form.get("query1")),
                "MonthlyCharges": float(request.form.get("query2")),
                "TotalCharges": float(request.form.get("query3")),
                "gender": request.form.get("query4"),
                "Partner": request.form.get("query5"),
                "Dependents": request.form.get("query6"),
                "PhoneService": request.form.get("query7"),
                "MultipleLines": request.form.get("query8"),
                "InternetService": request.form.get("query9"),
                "OnlineSecurity": request.form.get("query10"),
                "OnlineBackup": request.form.get("query11"),
                "DeviceProtection": request.form.get("query12"),
                "TechSupport": request.form.get("query13"),
                "StreamingTV": request.form.get("query14"),
                "StreamingMovies": request.form.get("query15"),
                "Contract": request.form.get("query16"),
                "PaperlessBilling": request.form.get("query17"),
                "PaymentMethod": request.form.get("query18"),
                "tenure": int(request.form.get("query19"))
            }

            # Convert to DataFrame
            df = pd.DataFrame([data])

            # One-hot encoding
            df = pd.get_dummies(df)

            # VERY IMPORTANT: Align columns with training data
            df = df.reindex(columns=model_columns, fill_value=0)

            # Predict
            prediction = model.predict(df)[0]
            prob = model.predict_proba(df)[0][1]

            result = "❌ Customer is likely to CHURN" if prediction == 1 else "✅ Customer will NOT churn"
            confidence = f"Confidence: {round(prob*100,2)}%"

            return render_template("homee.html",
                                   output1=result,
                                   output2=confidence)

        except Exception as e:
            return f"ERROR: {str(e)}"

    return render_template("homee.html")

if __name__ == "__main__":
    app.run(debug=True)

