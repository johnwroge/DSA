/*
A data structure where each element has a priority. Elements with higher priorities are served before
elements with lower priorities; can be implemented with an array or list, however it's slower 
    [p: 3, p: 1, p: 2, p: 5, p: 4];

so we are using a heap instead; 
works faster because retrieval is log(n);
we will be using a min binary heap because some systems treat lower numbers as higher priority than higher numbers

*/
class Node {
    constructor(val, priority){
        this.val = val;
        this.priority = priority; 
    }
}


class PriorityQueue{
    constructor (){
        this.values = []; 
        
    };

    enqueue (val, priority){
        let newNode = new Node(val, priority);
        this.values.push(newNode);
        this.bubbleUp(); 
    }

    bubbleUp (){
        let index = this.values.length - 1;
        const element = this.values[index];
        while (index > 0){
            let parentIndex = Math.floor((index - 1)/2);
            let parent = this.values[parentIndex];
            //this line changes because we need to compare priority
            if (element.priority >= parent.priority) break;
            this.values[parentIndex] = element;
            this.values[index] = parent; 
            index = parentIndex;
                }
        }
    sinkDown (){
        //declare an index variable initialized to 0 
        let index = 0;
        //get length of this.values store in variable for readability
        const length = this.values.length; 
        //get the element in the 0th position 
        const element = this.values[0];
        //loop while true
        while (true){
            //calculate left (2*index + 1) and right (2*index + 2)
            let left = 2*index + 1;
            let right = 2*index + 2;
            //intialize left and right child to undefined
            let leftChild, rightChild; 
            //create swap variable intitialzied to null
            let swap = null;
            //check if left is valid (less than length)
            if (left < length){
                //assign left child to be the value at the left index in this.values
                leftChild = this.values[left];
                //if leftchild is greater than element
                if (leftChild.priority < element.priority){
                    //reassign swap to be left
                    swap = left;
                }
            }
            //check if right is valid, less than length
            if (right < length){
                //reassign rightchild to be the element at the right index
                rightChild = this.values[right];
                //check if swap is null and right child is greater than element 
                //or if swap is not null and right child is greater than left child
                if (
                    (swap === null && rightChild.priority < element.priority) ||
                    (swap !== null && rightChild.priority < leftChild.priority)
                    )
                {//if true reassign swap to be right
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
    dequeue (){
        //store value of max = to first value
        const min = this.values[0];
        //store the last value as end, and remove it
        const end = this.values.pop();
        
        if (this.values.length > 0){
            this.values[0] = end; 
            this.sinkDown(); 
        }
        return min;
    }
}

let er = new PriorityQueue();
er.enqueue('common cold', 5)
er.enqueue('gunshot', 1)
er.enqueue('fever', 4)
er.enqueue('arm broke', 2)
er.enqueue('foot glass', 3)
console.log(er.dequeue())
console.log(er.dequeue())
console.log(er.dequeue())
console.log(er.dequeue())
console.log(er.dequeue())
console.log(er.dequeue())

