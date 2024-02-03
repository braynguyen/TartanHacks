

document.addEventListener('DOMContentLoaded', function () {
    // Initialize Cytoscape
    const cy = cytoscape({
      container: document.getElementById('cy'),
      elements: [
        { data: { id: 'node1', size: 30 }, position: { x: 100, y: 100 }, grabbable: false },
        { data: { id: 'node2', size: 50 }, position: { x: 300, y: 200 }, grabbable: false },
        { data: { id: 'edge1', source: 'node1', target: 'node2' } }
      ],
      style: [
        {
          selector: 'node',
          style: {
            'background-color': '#66ccff',
            'label': 'data(id)',
            'width': 'data(size)',
            'height': 'data(size)'
          }
        },
        {
          selector: 'edge',
          style: {
            'width': 3,
            'line-color': '#ccc',
            'target-arrow-color': '#ccc',
            'target-arrow-shape': 'triangle'
          }
        }
      ],
      layout: {
        name: 'preset' // Fixed positions layout
      }
    });
  
    // Add more customization or interactions here
  
    // Example: Zoom and Pan
    cy.zoom(1.5); // Zoom in
    cy.pan({ x: 100, y: 50 }); // Pan to a specific position
  
    // Example: Handle node click event
    cy.on('click', 'node', function (event) {
      const node = event.target;
      console.log('Clicked on node:', node.id());
    });
  });
  