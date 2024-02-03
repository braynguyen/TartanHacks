import logo from './logo.svg';
import './App.css';
import './components/TheMap'
import TheMap from './components/TheMap';

// information about the node data model:
// node: {
//   "val" --> determines the size of the bubble
//   "name" --> is what the hashtag would be
//   "id" ---> can be the hashtag because they are unique
// }
// link: {
//   source: "source of the edge"
//   target: "destination of the edge"
//   distance: "distance between source and target"
// }


const graphData = {
  nodes: [
    {"id": "id1", "name": "#booger", "val": 400},
    {"id": "id2", "name": "#bogger", "val": 42},
    {"id": "id3", "name": "#logger", "val": 10},
    {"id": "id4", "name": "#jogger", "val": 15},
    {"id": "id5", "name": "#fogger", "val": 20},
    // Adding the rest of the nodes up to 100
    ...Array.from({ length: 95 }, (_, i) => ({
      "id": `id${i + 6}`,
      "name": `#name${i + 6}`,
      "val": (i + 6) * 10
    }))
  ],
  links: [
    {"source": "id1", "target": "id2", "distance": 100},
    {"source": "id1", "target": "id3", "distance": 150},
    {"source": "id2", "target": "id4", "distance": 80},
    {"source": "id3", "target": "id4", "distance": 120},
    {"source": "id4", "target": "id5", "distance": 50},
    // Adding the rest of the links
    ...Array.from({ length: 94 }, (_, i) => ({
      "source": `id${i + 6}`,
      "target": `id${i + 7}`,
      "distance": (i + 7) * 2
    }))
  ]
};

function App() {

  

  return (
    <div className="App">
      <header className="App-header">
          <TheMap
            graphData={graphData}
            linkDistance={link => link.distance} // Use the 'distance' property to determine link lengths
          />
      </header>
    </div>
  );
}

export default App;
