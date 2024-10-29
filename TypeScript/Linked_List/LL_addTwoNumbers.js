/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
*/


const addTwoNumbers = (l1, l2) => {
    //create a result node and assign it to a new node with value of -1
    let result = new Node(-1);
    //create a dummy and assign it to result node
    let dummy = result;
    //create a carry variable initialized to 0
    let carry = 0;
    //loop while l1, l2, or carry is truthy
    while (l1 || l2 || carry){
        //get the l1 value by using conditional 
            let l1Val = l1 ? l1.val : 0; 
        //get the l2 value by using conditional
            let l2Val = l2 ? l2.val : 0;
        //get next digit, which should be l1 val + l2 val + carry val modulo 10 
            let nextDigit = (l1Val + l2Val + carry) % 10;
        //assign result.next to be a new node with next digit 
            result.next = new Node(nextDigit);
        //assign result to be result.next (moving pointer)
            result = result.next;
        //reassign carry to be the l1 val + l2 + previous carry divided by 10
            carry = Math.floor((l1Val +l2Val + carry) / 10);
        //if l1, reassign l1 to be l1.next or 0 if not
            l1 = l1 ? l1.next: 0;
        //if l2, reassing l2 to be next if truthy or 0 if not
            l2 = l2 ? l2.next : 0; 
    }
    //return the dummy.next linked list
    return dummy.next; 
}










// var addTwoNumbers = function(l1, l2) {
//     let node = null
//     const carry = arguments[2]
//     if (l1 || l2) {
//         const val1 = l1 ? l1.val : 0
//         const val2 = l2 ? l2.val : 0
//         const next1 = l1 ? l1.next : null
//         const next2 = l2 ? l2.next : null
//         const val = carry ? val1 + val2 + 1 : val1 + val2
//         node = new ListNode(val % 10)
//         node.next = addTwoNumbers(next1, next2, val >= 10)  
//     } else if (carry) {
//         node = new ListNode(1)
//         node.next = null
//     }
//     return node
// };



// function LinkedList() {
//     this.head = null;
//     this.tail = null; 
//   }
  
//   // NOTE: needs to be es5 function definition
//   function Node(val) {
//     this.val = val;
//     this.next = null;
//   }


// const addTwoNumbers =(l1, l2) => {

    


// }

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
//  * @param {ListNode} l1
//  * @param {ListNode} l2
//  * @return {ListNode}
 */
//  var addTwoNumbers = (l1, l2) => {
//     let n1 = [l1.val], n2 = [l2.val];
    
//     let node1 = l1.next, node2 = l2.next;
    
//     while (node1) {
//         n1.unshift(node1.val);
//         node1 = node1.next;
//     }
    
//     while (node2) {
//         n2.unshift(node2.val);
//         node2 = node2.next;
//     }
    
//     const res = (BigInt(n1.join(``)) + BigInt(n2.join(``))).toString();
    
//     return res.split(``).slice(1).reduce((head, val) => new ListNode(val, head), new ListNode(res[0]));
// };