from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    data = {'today_tds': int(np.random.randint(1000)),
        'today_usage': int(np.random.randint(1000)),
        'tds_history': [int(tmp) for tmp in np.random.randint(1000, size=7)],
        'usage_history': [int(tmp) for tmp in np.random.randint(1000, size=7)]}
    return jsonify(data)

@app.route('/map', methods=['GET'])
def map():
    import json
    data = json.load(open('map_data.json', 'r'))

    return jsonify(data)

@app.route('/tds', methods=['POST'])
def update_tds():
    tds = float(request.form['tds'])
    with open('tds.txt', 'a+') as ftds:
        ftds.write('{}\n'.format(tds))
        return jsonify({'message': 'success'})

@app.route('/usage', methods=['POST'])
def update_usage():
    usage = float(request.form['usage'])
    with open('usage.txt', 'a+') as fusage:
        fusage.write('{}\n'.format(usage))
        return jsonify({'message': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
