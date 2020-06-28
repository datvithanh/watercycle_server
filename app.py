from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    tds = [float(tmp) for tmp in open('tds.txt', 'r').readlines()[-7:]]
    usage = [float(tmp) for tmp in open('usage.txt', 'r').readlines()[-7:]]
    data = {'today_tds': tds[-1],
        'today_usage': usage[-1],
        'tds_history': tds,
        'usage_history': usage}

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
