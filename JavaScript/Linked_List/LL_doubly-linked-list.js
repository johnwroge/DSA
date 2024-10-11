/*
  * Below, you are provided the construtors for a doubly linked list as well as a constructor for the nodes it's composed of
  * Construct a doubly linked list & modify it's prototype to contain methods named 'add' and 'remove'
  * The 'add' method should add an additional node to the end of the doubly linked list
  * The 'remove' method should remove the first instance of a node containing a specific value from the doubly linked list
  
  Example doubly linked list
  null <-> 4 <-> 9 <-> 2 <-> 1 <-> null

  Example after using 'add' method to add 6
  null <-> 4 <-> 9 <-> 2 <-> 1 <-> 6 <-> null

  Example after using 'remove' method to remove 2
  null <-> 4 <-> 9 <-> 1 <-> 6 <-> null

  NOTE: must use non-arrow functions for object constructors and prototype methods
  @see: https://dmitripavlutin.com/when-not-to-use-arrow-functions-in-javascript/
*/

function DoublyLinkedList() {
  this.head = null;
  this.tail = null;
}

function Node(val) {
  this.val = val;
  this.next = null;
  this.prev = null;
}

/*
This method should add a node to the end of the doubly linked list
 */
DoublyLinkedList.prototype.add = function (val) {
  //create a constant variable new node
  const node = new Node(val);
  //check if there isn't a head 
  if (!this.head){
    //reassign the head and tail to be the new node
    this.head = node;
    this.tail = node; 
    return this; 
  } else {
  //otherwise, 
    //store the current tail in a variable
    let previous = this.tail;
    //assign variable.next to be the new Node
    previous.next = node; 
    //reassign the tail to be the new node
    this.tail = node;
    //reassigning the prev value on the new node to be prev
    node.prev = previous; 
    return this; 
  }
};

/*
This method should remove the first instance of a node with the inputted value from the doubly linked list
 */
DoublyLinkedList.prototype.remove = function (val) {
    let current;
    let previous;
    let temp; 

    if (this.head.val === val){
      
      current = this.head.next;
      current.prev = null;
      this.head.next = null;
      this.head.prev = null; 
      this.head = current;  
    }
    else if (this.tail.val === val){
      previous = this.tail.prev; 
      previous.next = this.tail.next; 
      this.tail.next = null; 
      this.tail.prev = null;
      this.tail = previous;
      } 
      else {
        current = this.head; 
        previous = current; 
        while (current.next){
          previous = current; 
          current = current.next;
          if (current.val === val){
            previous.next = current.next;
            temp = current.next; 
            temp.prev = previous;
            current.prev = null;
            current.next = null;
          }
        }
        return temp === undefined ? -1 : this; 
      }
    } ;




module.exports = { DoublyLinkedList, Node };