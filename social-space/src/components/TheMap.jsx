import { useState, useEffect, useRef } from 'react';
import { ForceGraph3D, ThreeJSForceGraph } from 'react-force-graph';
import * as THREE from 'three'; // Import the 'three' library


// Corrected the function component definition and destructuring props
export default function TheMap({ graphData }) {
    const [selectedNode, setSelectedNode] = useState(null); // State to hold the selected node
    const [embed, setEmbed] = useState(null); // State to store the TikTok embed
    const [searchedNode, setSearchedNode] = useState(null); // for search node for later

    // refs
    const fgRef = useRef(); // Reference to the ForceGraph3D component

    useEffect(() => {
        if (fgRef.current) {
          // Increase the charge strength to repel nodes
          fgRef.current.d3Force('charge').strength(-1250); // Experiment with the value
        }
      }, []);


    // Handler for node click events
    const handleNodeClick = node => {
        setSelectedNode(node); // Update state with the clicked node's data
        handleNodeZoom(node);
    };

    // Function to close the popup
    const handleClosePopup = () => {
        setSelectedNode(null); // Clear the selected node to hide the popup
    };

    const handleNodeZoom = node => {
        // Aim at node from outside it
        const distance = 40;
        const distRatio = 1 + distance/Math.hypot(node.x, node.y, node.z);

        fgRef.current.cameraPosition(
            { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio }, // new position
            node, // lookAt ({ x, y, z })
            3000  // ms transition duration
        );
    }


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
                ref={fgRef}
                graphData={graphData}
                onNodeClick={handleNodeClick}
                enableNodeDrag={false}
                showNavInfo={true}
                linkOpacity={0.1}
                nodeOpacity={0.85}
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
