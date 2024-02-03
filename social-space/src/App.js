import logo from './logo.svg';
import './App.css';
import './components/TheMap';
// import Button from '@mui/joy/Button';
import ToggleButton from '@mui/material/ToggleButton'; // Correct import statement

import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import TheMap from './components/TheMap';
import { useState, useEffect } from 'react';
import { slide as Menu } from 'react-burger-menu';
import Search from './components/search'; // Import the Search component


function App() {
  const [graphData, setGraphData] = useState({ nodes: [], links: [] });
  const [menuOpen, setMenuOpen] = useState(false);
  const [contentMode, toggleMode] = useState(false); // can be content:true or user:false

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        console.log("fetching");
        var response = '';
        if(contentMode){
          response = await fetch('http://localhost:5000/api/graph-data');
        } else {
          response = await fetch('http://localhost:5000/api/graph-user-data');
          console.log('fetching user data')
        }

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setGraphData(data);
      } catch (error) {
        console.error("Could not fetch graph data:", error);
      }
    };
    fetchGraphData();
  }, [], [contentMode]);

  const handleMenuButtonClick = () => {
    setMenuOpen(!menuOpen);
  };

  const inviteFriend = () => {
    // Add your logic for inviting friends here
    alert("Invite your friend!");
  };

  const handleUserToggle = () => {
    toggleMode(!contentMode);
  }

  return (
    <div className="App">
      <Menu isOpen={menuOpen} width={250} right onStateChange={({ isOpen }) => setMenuOpen(isOpen)}>
        {/* Add your menu items here */}
        <div>
          <h2>Social Space</h2>
          <ToggleButtonGroup
              exclusive
              onChange={(event, newValue) => {
                if (newValue !== null) {
                  console.log('change mode');
                  toggleMode(!contentMode);
                }
              }}
            >
              <ToggleButton value="General" style={contentMode ? { backgroundColor: '#d3d3d3' } : {}}>
                General
              </ToggleButton>
              <ToggleButton value="User" style={!contentMode ? { backgroundColor: '#d3d3d3' } : {}}>
                User
              </ToggleButton>
          </ToggleButtonGroup>

          <p><b>My Top Tags</b></p>
          <hr />
          <ol>
            <li><a onClick={() => setMenuOpen(false)} href="/">#BookTok</a></li>
            <li><a onClick={() => setMenuOpen(false)} href="/">#Pickleball</a></li>
            <li><a onClick={() => setMenuOpen(false)} href="/">#Cooking</a></li>
          </ol>
        </div>
        <div>
          <p><b>My Toks</b></p>
          <hr />
          <ol>
            <li><a onClick={() => setMenuOpen(false)} href="/">BookTok</a></li>
            <li><a onClick={() => setMenuOpen(false)} href="/">CookTok</a></li>
            <li><a onClick={() => setMenuOpen(false)} href="/">PickleballTok</a></li>
          </ol>
        </div>
        <div className='bottom'>
          <button className="invite-button" onClick={inviteFriend}>Invite Friend</button>
          <Search/>
        </div>
      </Menu>
      <TheMap
        graphData={graphData}
        linkDistance={link => link.distance}
        zIndex={1}
      />
    </div>
  );
}

export default App;
