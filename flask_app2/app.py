from flask import Flask, render_template
import sys, os
import numpy as np

# Tambahkan path agar Flask tahu lokasi folder matrix_regression
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from matrix_regression.matrix import Matrix
app = Flask(__name__)

@app.route('/')
def index():
    file_path = '/app/data/suhu.csv'
    matrix = Matrix.from_csv(file_path)

    transpose = matrix.transpose()
    try:
        inverse = matrix.inverse()
    except np.linalg.LinAlgError:
        inverse = "Matrix tidak dapat di-invers (determinannya 0)"

    # regresi sederhana (x, y)
    data = np.loadtxt(file_path, delimiter=",")
    x = data[:, 0].reshape(-1, 1)
    y = data[:, 1]
    from sklearn.linear_model import LinearRegression
    model = LinearRegression().fit(x, y)
    pred_y = model.predict(x)

    return render_template(
        'index.html',
        original=matrix.data.tolist(),
        transpose=transpose.data.tolist(),
        inverse=str(inverse),
        coef=model.coef_[0],
        intercept=model.intercept_,
        predictions=pred_y.tolist()
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

