import { useState, useEffect } from 'react';
import { ForceGraph3D } from 'react-force-graph';

// Corrected the function component definition and destructuring props
export default function TheMap({ graphData: graphData }) {
    const [selectedNode, setSelectedNode] = useState(null); // State to hold the selected node

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
                    color: 'black'
                }}>
                    <div>Id: {selectedNode.id}</div>
                    <div>Name: {selectedNode.name}</div>
                    <div>Value: {selectedNode.val}</div>
                    <div>Links: ? {selectedNode.video_links[0]}</div>
                    
                    <button onClick={handleClosePopup}>Close</button>
                </div>
            )}
        </>
    );
}
