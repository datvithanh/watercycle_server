from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/dashboard')
def dashboard():
    data = {'today_tds': int(np.random.randint(1000)),
        'today_usage': int(np.random.randint(1000)),
        'tds_history': [int(tmp) for tmp in np.random.randint(1000, size=30)],
        'usage_history': [int(tmp) for tmp in np.random.randint(1000, size=30)]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
