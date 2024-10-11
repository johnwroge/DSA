/*
Write a function to delete the first instance of a node in a singly linked list.
The function should return the deleted node, or undefined if the value was not found.

Example: 
Given a linked list:
 
('a' -> 'b' -> 'c' -> 'b' -> 'd')
 
And given a value, 'b', the linked list after calling your function should look like:

('a' -> 'c' -> 'b' -> 'd')

And the evaluated result would be the removed node with the value of 'b'.

How might you remove a linked list value without adding extra properties to the constructor functions?

*/

// NOTE: needs to be es5 function definition
function LinkedList() {
  this.head = null;
}

// NOTE: needs to be es5 function definition
function Node(val) {
  this.val = val;
  this.next = null;
}

const linkedListRemove = (ll, val) => {
  if (!ll || !val) return undefined; 
  let current = ll.head; 
  let prev;
  let result = undefined; 
    while (ll){ 
      prev = current;
      current = current.next; 
    }
    if (current.val === val){
      prev.next = current.next;
      current.next = null;
      return current;
    }

  return undefined; 
};
const ll = new LinkedList();
const nodeList = new Node('a');
    nodeList.next = new Node('d');
    nodeList.next.next = new Node('b');
    nodeList.next.next.next = new Node('c');
    nodeList.next.next.next.next = new Node('b');
    ll.head = nodeList;
console.log(linkedListRemove(ll, 'b'))


/*
Extension: 
* Write a function to delete the first instance of a node in a singly linked list with a space complexity of O(1). 
* Write a function to delete the all instances of a node in a singly linked list.

Example: 
Given a linked list:
 
('a' -> 'b' -> 'd' -> 'c' -> 'd')
 
 And given a value, 'd', the evaluated result of calling your function should be:

 ('a' -> 'b' -> 'c')

*/

const linkedListRemoveMultiple = (ll, val) => {

}

module.exports = { LinkedList, Node, linkedListRemove, linkedListRemoveMultiple };
