from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/graph-data', methods=['GET'])
def get_graph_data():
    # Preparing the graph data
    nodes = [
        {"id": "id1", "name": "#booger", "val": 400},
        {"id": "id2", "name": "#bogger", "val": 42},
        {"id": "id3", "name": "#logger", "val": 10},
        {"id": "id4", "name": "#jogger", "val": 15},
        {"id": "id5", "name": "#fogger", "val": 20},
    ] + [{"id": f"id{i+6}", "name": f"#name{i+6}", "val": (i+6) * 10} for i in range(95)]

    links = [
        {"source": "id1", "target": "id2", "distance": 100},
        {"source": "id1", "target": "id3", "distance": 150},
        {"source": "id2", "target": "id4", "distance": 80},
        {"source": "id3", "target": "id4", "distance": 120},
        {"source": "id4", "target": "id5", "distance": 50},
    ] + [{"source": f"id{i+6}", "target": f"id{i+7}", "distance": (i+7) * 2} for i in range(94)]

    graph_data = {"nodes": nodes, "links": links}

    # Returning the graph data as JSON
    return jsonify(graph_data)

if __name__ == '__main__':
    app.run(debug=True)
