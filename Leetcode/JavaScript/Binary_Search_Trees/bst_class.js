


function TreeNode(val, left, right) {
    this.val = val; 
    this.left = null;
    this.right = null; 
}

TreeNode.prototype.add = function(val){
    const node = new TreeNode(val);
  
    if (!this.val){
        this.val = node; 
    } 
    if (val < this.val){   
        if (!this.left){
            this.left = node;
        } else {
            this.left.add(val)
        }
    }
    if (val > this.val){
        if (!this.right){
            this.right = node;
        } else {
            this.right.add(val)
        }
    }
}



TreeNode.prototype.BFS =  function () {
    let queue = [this];
    const result = [];
    while (queue.length){
        let current = queue.shift();
        if (!current) break; 
        if (current.left) queue.push(current.left);
        result.push(current.val)
        if (current.right) queue.push(current.right);
    }
return result; 
}

TreeNode.prototype.DFS = function () {
    console.log(this)
    let queue = [this];
    const result = [];
    while (queue.length){
        let current = queue.pop();
        console.log(current.val)
        if (current.left) queue.push(current.left);
        
        if (current.right) queue.push(current.right);
    }
return result; 
}


function Stack(){
    this.storage = {};
    this.index = 0;
}

Stack.prototype.enqueue = function (value){
    this.storage[this.index] = value; 
    ++this.index;
    return this; 
}

Stack.prototype.dequeue = function (){
    let index = this.index - 1; 
    let temp = this.storage[index];
    delete this.storage[index];
    --this.index;
    return temp
}






    
let bst = new TreeNode(2);

bst.add(1)
bst.add(3)
bst.add(6)
bst.add(4)
bst.add(8)
bst.add(7)
bst.add(9)
bst.add(10)

console.log(bst.DFS())
