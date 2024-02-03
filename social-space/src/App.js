import logo from './logo.svg';
import './App.css';
import './components/TheMap'
import TheMap from './components/TheMap';
import { useState, useEffect, useRef } from 'react';
import { slide as Menu } from 'react-burger-menu'; // Import the Slide component


// Import the menuStyles.css
// import './styles/menuStyles.css';
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

function App() {
  const [graphData, setGraphData] = useState({ nodes: [], links: [] });
  const [menuOpen, setMenuOpen] = useState(false); // State to control menu open/close

    useEffect(() => {
      // Define the function to fetch graph data
      const fetchGraphData = async () => {
          try {
              console.log("fetching")
              const response = await fetch('http://localhost:5000/api/graph-data');
              if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
              }
              const data = await response.json();
              setGraphData(data);
          } catch (error) {
              console.error("Could not fetch graph data:", error);
          } 
      };
      // Call the fetch function
      fetchGraphData();
  }, []); // empty dependency array to run on component mount

  // Function to handle menu button click
  const handleMenuButtonClick = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <div className="App">
      {/* <header className="App-header"> */}
        <Menu isOpen={menuOpen} width={250} right onStateChange={({ isOpen }) => setMenuOpen(isOpen)}>
          {/* Add your menu items here */}
          <a onClick={() => setMenuOpen(false)} href="/">Home</a>
          <a onClick={() => setMenuOpen(false)} href="/about">About</a>
          <a onClick={() => setMenuOpen(false)} href="/contact">Contact</a>
        </Menu>


          <TheMap
            graphData={graphData}
            linkDistance={link => link.distance}
            zIndex={1}
          />
      {/* </header> */}
    </div>
  );
}

export default App;
