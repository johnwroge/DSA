/* Pseudocode */

//iterative
var reverseList = function(head) {
    if (!head) return head;
    let curr = head;
    let prev = null;
    while (curr){
        let temp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = temp;
    }
    return head; 
    }
//recursive
    var reverseList = function(head) {
        // if head is null or next is null return the head

        //create a variable res and assign to evalutated result of invoking function with head.next
        var res = reverseList(head.next);

        //reassign head nextnext to head
        head.next.next = head;
        //set head's next to be null...
        head.next = null;
        // Return the reverse linked list...
        return res;     
    };