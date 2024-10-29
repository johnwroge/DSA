
// undirected and unweight graph for flights, city to city 
//added type: module to package.json to allow export/import

export class Graph {
    constructor(){
        this.adjacencyList = {}
    }

    addVertex(vertex){
        if (!this.adjacencyList[vertex])
        this.adjacencyList[vertex] = [];
    }

    addEdge(v1, v2){
        // find key of vertex 1 in adjacency list and push vertex2 into the array
        if (this.adjacencyList[v1]){
            this.adjacencyList[v1].push(v2);
        }
        //find key of vertex 2 and push vertex1 into the array
        if (this.adjacencyList[v2]){
            this.adjacencyList[v2].push(v1);
        }
    }
    removeEdge(v1,v2){
        if (this.adjacencyList[v1]){
            let current = this.adjacencyList[v1].filter(el => el !== v2);
            this.adjacencyList[v1] = current;
        }

        if (this.adjacencyList[v2]){
            let current = this.adjacencyList[v2].filter(el => el !== v1);
            this.adjacencyList[v2] = current;
          
        }
    }
    removeVertex(vertex){
        this.adjacencyList[vertex].forEach(element => {
            this.removeEdge(vertex, element)
        });
        delete this.adjacencyList[vertex];
    }

    RecursiveDFS (start){
        const results = [];
        const visited = {};
        const dfs = (vertex) => {
            if (!vertex) return;
            results.push(vertex)
            visited[vertex] = "true"
            for (let i = 0; i < this.adjacencyList[vertex].length; i++){
                const neighbor = this.adjacencyList[vertex][i];
                if (!visited[neighbor]){
                    dfs(neighbor)
                }
            }
        }
    dfs(start);
    return results; 
    }

    IterativeDFS (start){
        let stack = [];
        let results = [];
        const visited = {};
        stack.push(start);
        while (stack.length){
            const vertex = stack.pop();
            if (!visited[vertex]){
                results.push(vertex);
                visited[vertex] = true;
                this.adjacencyList[vertex].forEach(neighbor => 
                    stack.push(neighbor)
                )
            }
        }
        return results; 
    }

    IterativeBFS (start){
        let queue = [start];
        let results = [];
        const visited = {};
        while (queue.length){
            const vertex = queue.shift();
            if (!visited[vertex]){
                results.push(vertex);
                visited[vertex] = true;
                this.adjacencyList[vertex].forEach(neighbor => 
                    queue.push(neighbor)
                )
            }
        }
        return results; 

    }

}






const g = new Graph();

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")


g.addEdge("A","B")
g.addEdge("A","C")
g.addEdge("B","D")
g.addEdge("C","E")
g.addEdge("D","E")
g.addEdge("D","F")
g.addEdge("E","F")

//console.log(g.RecursiveDFS("A"))
// console.log(g.IterativeDFS("A"))
// console.log(g.IterativeBFS("A"))
//DFS: recursive: uses call stack to keep track of everything
/*
    //function should accept a node
        //create a list or array to be returned
        create object to store visited vertices
        //dfs helper
        //invoke helper function with starting vertex
        //return result array
DFS Helper function(vertex):
   base case: if vertex is empty
        return 
    add vertex to results list
    mark vertex as visited (in object or array)
    for each neighbor in vertex's neighbors:
        if neighbor is not visited: 
            recursively call DFS on neighbor
*/

/*
DFS-Iterative
//defined a function that takes a start value
    Let s be a stack
    push the start into the stack
    //while the stack is not empty
        //pull the last element from the stack
        //if the vertex is not discoverd
            //visit vertex and add to result list
            //label vertex as discovered
            //for each of vertex's neighbords, push each onto the stack. 
*/


const findOrder = (numCourses, prerequisites) => {
    const inDegrees = Array(numCourses).fill(0);
    for (const [v] of prerequisites) {
      inDegrees[v]++;
    }

    console.log(inDegrees)
  
    const q = [];
    for (let i = 0; i < inDegrees.length; i++) {
      const degree = inDegrees[i];
      if (degree === 0) q.push(i);
    }
  
    const res = [];
    while (q.length) {
      const u0 = q.shift();
      numCourses--;
      res.push(u0);
      for (const [v, u] of prerequisites) {
        if (u === u0) {
          inDegrees[v]--;
          if (inDegrees[v] === 0) q.push(v);
        }
      }
    }
    return numCourses === 0 ? res : [];
  };

  console.log(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))