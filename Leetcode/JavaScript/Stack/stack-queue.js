/**
 * 
 * First, create a Stack which contains the following methods:
 * - push: add value to top (end) of stack
 * - pop: remove value from top (end) of stack
 * 
 * Second, create a Queue which consists of two stacks: stack1 and stack2
 * and contains the following methods:
 * - enqueue: add value to queue
 * - dequeue: remove value from queue
 * Queue methods should follow First In, First Out rule.
 * 
 * DO NOT USE NATIVE JS METHODS
 * 
 */

 function Stack() {
    this.stack = {};
    this.length = 0;
  }
  
  Stack.prototype.push = function(value) {
    let index = this.length;
    this.stack[index] = value;
    console.log(this.stack)
    this.length += 1;
    return this.stack;
  };
  
  
  Stack.prototype.pop = function(){
    if (this.stack[0] === undefined) return undefined;
    const ourIndex = this.length - 1;
    const stringIndex = JSON.stringify(ourIndex);
    lastVal = this.stack[stringIndex];
    delete this.stack[stringIndex];
    this.length--;
    return lastVal;
  }


  function Queue() {
    this.storage = {};
    let stack1 = new Stack();
    let stack2 = new Stack();
    this.index = 0;
    this.head = 0;
    this.tail = 0;
}

Queue.prototype.enqueue = function(value) {
    let index = this.index;
    this.storage[index] = value;
    this.index += 1;
    this.tail += 1;
    return this.storage;
};  

Queue.prototype.dequeue = function() {
  
    if (this.storage[this.head] === undefined) return undefined;
    const item = this.storage[this.head];
    delete this.storage[this.head];
    this.head++;
    return item;
};

module.exports = { Stack, Queue };
