import { useState, useEffect } from 'react';
import { ForceGraph3D } from 'react-force-graph';

// Corrected the function component definition and destructuring props
export default function TheMap({ graphData }) {
    const [selectedNode, setSelectedNode] = useState(null); // State to hold the selected node
    const [embed, setEmbed] = useState(null); // State to store the TikTok embed

    // Handler for node click events
    const handleNodeClick = node => {
        setSelectedNode(node); // Update state with the clicked node's data
    };

    // Function to close the popup
    const handleClosePopup = () => {
        setSelectedNode(null); // Clear the selected node to hide the popup
    };

    useEffect(() => {
        const fetchEmbed = async () => {
            try {
                const res = await fetch('https://www.tiktok.com/oembed?url=' + selectedNode.video_links[0]);
                const data = await res.json();
                setEmbed(data.html);
                console.log(data.html);
                console.log(data);
            } catch (error) {
                console.error('Error fetching TikTok embed:', error);
                setEmbed(null);
            }
        };

        if (selectedNode) {
            fetchEmbed();
        }
    }, [selectedNode]);

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
                    <div dangerouslySetInnerHTML={{ __html: embed }}></div>

                    <button onClick={handleClosePopup}>Close</button>
                </div>
            )}
        </>
    );
}
