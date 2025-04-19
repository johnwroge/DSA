

class DirectedGraph {
    constructor() {
      this.adjacencyList = new Map();
    }
  
    addVertex(vertex) {
      if (!this.adjacencyList.has(vertex)) {
        this.adjacencyList.set(vertex, []);
      }
    }
  
    addEdge(source, destination) {
      if (!this.adjacencyList.has(source)) {
        this.adjacencyList.set(source, []);
      }
      this.adjacencyList.get(source).push(destination);
    }
  
    getNeighbors(vertex) {
      return this.adjacencyList.get(vertex);
    }
  
    getVertices() {
      return [...this.adjacencyList.keys()];
    }
  
    getEdges() {
      const edges = [];
      for (const [vertex, neighbors] of this.adjacencyList.entries()) {
        for (const neighbor of neighbors) {
          edges.push([vertex, neighbor]);
        }
      }
      return edges;
    }
  }
  
  // Example usage:
//   const graph = new DirectedGraph();
//   graph.addVertex('A');
//   graph.addVertex('B');
//   graph.addVertex('C');
//   graph.addEdge('A', 'B');
//   graph.addEdge('B', 'C');
//   console.log(graph.getNeighbors('A')); // Output: ['B']
//   console.log(graph.getEdges()); // Output: [['A', 'B'], ['B', 'C']]



console.log(buildAdjacencyList([[1,0],[2,0],[3,1],[3,2]]))

  function buildAdjacencyList (courses) {
    const adjList = new Map();
    for (let i = 0; i < courses.length; i++){ 
        const [first, second] = courses[i];
        if (!adjList.has(first)){
            adjList.set(first, []);
            addEdge(adjList, first, second)
        }
        if (!adjList.has(second)){
            adjList.set(second, []);
        }
    }

    function addEdge (adj, source, destination){
    adj.get(source).push(destination);
    return; 
}

    return adjList; 
 }
