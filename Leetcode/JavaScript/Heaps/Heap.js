class MaxBinaryHeap {
    constructor(){
        this.values = [];
    }
    insert(val){
        this.values.push(val);
        this.bubbleUp()
    }
    bubbleUp(){
        let index = this.values.length - 1; 
        let element = this.values[index];

        while (index > 0){
            let parentIndex = Math.floor((index - 1) / 2);
            let parent = this.values[parentIndex];
            if (element <= parent) break; 
            [this.values[parentIndex], this.values[index]] = [this.values[index], this.values[parentIndex]]
            index = parentIndex;
        }

    }
    // highest priority item is removed with this method (the root)
    extractMax(){
        [this.values[0], this.values[this.values.length - 1]] = [this.values[this.values.length - 1], this.values[0]]
        let max = this.values.pop()
        this.sinkDown()
    }

    sinkDown (){
        //declare an index variable initialized to 0 
        let index = 0; 
        //get length of this.values store in variable for readability
        let length = this.values.length; 
        //get the element in the 0th position 
        let element = this.values[0];
        //loop while true
        while (true){
            //calculate left (2*index + 1) and right (2*index + 2)
            let left =  2 * index + 1; 
            let right = 2 * index + 2; 
            //intialize left and right child to undefined
            let leftChild, rightChild; 
            //create swap variable intitialzied to null
            let swap = null; 
            //check if left is valid (less than length)
            if (left < length){
                //assign left child to be the value at the left index in this.values
                leftChild = this.values[left];
                //if leftchild is greater than element
                if (leftChild > element){
                    //reassign swap to be left
                    swap = left; 
                }
            }
            //check if right is valid, less than length
            if (right < length){
                 //reassign rightchild to be the element at the right index
                 rightChild = this.values[right];
                 //check if swap is null and right child is greater than element 
                 if (swap === null && rightChild > element ||
                     //or if swap is not null and right child is greater than left child
                     swap !== null && rightChild > leftChild
                    ){//if true reassign swap to be right
                        swap = right; 
                    }  
            }
            
            //check if swap is null (no swaps happened then you found right position)
            if (swap === null) break; 
            //assign the value at the index to be the value at the swap index
            this.values[index] = this.values[swap];
            //assign the value at the swap index to be the element
            this.values[swap] = element; 
            //reassign the index to be the swap index; 
            index = swap; 
        }
    }
}

let heap = new MaxBinaryHeap()

heap.insert(10)
heap.insert(15)
heap.insert(5)
heap.insert(1)
heap.insert(100)
heap.insert(20)
heap.insert(6)
console.log(heap)