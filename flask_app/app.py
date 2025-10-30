import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, jsonify
from matrix_regression.matrix import Matrix
from matrix_regression.regression import LinearRegressionMatrix
import json

app = Flask(__name__)

# Baca data suhu dari CSV
data = Matrix.from_csv("../data/matriks.csv").data
hari = data[:, 0].reshape(-1, 1)
suhu = data[:, 1].reshape(-1, 1)

# Latih model regresi
model = LinearRegressionMatrix(hari, suhu)
model.fit()

@app.route("/")
def index():
    # Kirim data suhu aktual ke frontend
    suhu_data = [{"hari": int(h), "suhu": float(s)} for h, s in zip(hari.flatten(), suhu.flatten())]
    return render_template("index.html", suhu_data=json.dumps(suhu_data))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        hari_input = float(request.form["hari"])
        prediksi = model.predict([[hari_input]])[0][0]
        return jsonify({"prediksi": round(prediksi, 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

