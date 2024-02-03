import { useState, useEffect } from 'react';
import { ForceGraph3D } from 'react-force-graph';

// Corrected the function component definition and destructuring props
export default function TheMap({ graphData: initialGraphData }) {
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });
    const [selectedNode, setSelectedNode] = useState(null); // State to hold the selected node

    useEffect(() => {
        // Define the function to fetch graph data
        const fetchGraphData = async () => {
            try {
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


    // Handler for node click events
    const handleNodeClick = node => {
        setSelectedNode(node); // Update state with the clicked node's data
    };

    // Function to close the popup
    const handleClosePopup = () => {
        setSelectedNode(null); // Clear the selected node to hide the popup
    };

    return (
        <>
            <ForceGraph3D
                graphData={graphData}
                onNodeClick={handleNodeClick}
            />
            {selectedNode && (
                <div style={{
                    position: 'absolute',
                    top: '20%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)',
                    backgroundColor: 'white',
                    padding: '20px',
                    zIndex: 100,
                    border: '1px solid #ddd',
                    borderRadius: '8px',
                    boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
                }}>
                    <div>Id: {selectedNode.id}</div>
                    <div>Name: {selectedNode.name}</div>
                    <div>Value: {selectedNode.val}</div>
                    <button onClick={handleClosePopup}>Close</button>
                </div>
            )}
        </>
    );
}
