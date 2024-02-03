from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # You can replace the data with your populated data when ready
    data = {"id": "id1", "name": "#booger", "val": 400}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
