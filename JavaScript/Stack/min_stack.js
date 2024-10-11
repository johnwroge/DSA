/*
155. Min Stack
Medium
11.4K
726
Companies
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.


*/


var MinStack = function() {
    this.stack = {};
    this.length = 0; 
};

/** 
 * @param {number} val
 * @return {void}
 */


MinStack.prototype.push = function(val) {
    this.stack[this.length] = val; 
    ++this.length;
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    let index = this.length - 1;
    let popped = this.stack[index];
    this.length--;
    delete this.stack[index];
    return popped; 
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    let index = this.length - 1;
    let top = this.stack[index];
    return top; 
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return Math.min(...Object.values(this.stack))
};

let obj = new MinStack();
obj.push(3)
obj.push(2)
obj.push(1)
// obj.pop()
// var param_3 = obj.top()
// var param_4 = obj.getMin()

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */