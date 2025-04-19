/*
684. Redundant Connection
Medium
5.2K
352
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles. (acyclic)

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge 
added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
 The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that 
 there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
 return the answer that occurs last in the input.

 

Example 1:

Questions for charles, can an undirected graph have cycles? i.e. do cycles only exist in 
a directed graph


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
*/


//soln 1

// var findRedundantConnection = function(edges) {
//     let par = Array.from({length: edges.length + 1}, (_,i) => i)
//     const find = x => x === par[x] ? par[x] : par[x] = find(par[x])
//     const union = (x,y) => par[find(y)] = find(x)
//     for (let [a,b] of edges)
//         if (find(a) === find(b)) return [a,b]
//         else union(a,b)
// };

//soln 2

var findRedundantConnection = function(edges) {
    //create an object to store -
    const uf = {};
    //iterate over the edges
    for (let edge of edges){
        //for each edge destructure u and v as 0th and 1st index
       let [u, v] = edge;
        //check if evaluating find helper function with u is equal to evaluated result of v
        //check if edges two vertices are already connected by finding their corresponding set using find helper function
       if (find(u) === find(v)){
        
            //if they are already connected, return that edge
        return edge;
       } else {
            //otherwise connect the two vertices by merging their sets -> invoke union helper function with u and v
        union(u,v)
       }      
    } 
    
    //create union helper function that takes two values a,b
        //union function merges two sets by setting the value of the 
        //find result for one set to the find result of the other set.
    function union(a, b){ 
        //create a key in object of evaluated result of invoking find with a and assign it to the value of the value at the key of 
        //invoking find function with b ... ?
        uf[find(a)] = uf[find(b)] 
    }
    //The find function recursively searches for the representative element (also called the root) of the set 
    //containing a given element and performs path compression to optimize future searches.
    function find(x){
        //check if there is not a key of x in object, if true create a key of the x and a value of x
        console.log(uf)
        if (!uf[x]) uf[x] = x;
        //check if the key of x in the object is equal to x, return x
        if (uf[x] === x) return x; 
        //return original function passing in the value at the key of x in the object
        return find(uf[x])
    }
}

console.log(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))