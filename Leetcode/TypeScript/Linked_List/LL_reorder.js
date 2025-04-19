/*
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
//  var reorderList = function(head) {
    
//     //create an array to store the nodes
//     const result = [];
//     //create a left and right pointer
//     let left = 0;
//     //create a flag variable and assign to true
//     let flag = true;
//     //iterate over the linked list
//     while (head){
//         //push each node into the array
//         result.push(head.val);
//         head = head.next; 
//     }
//     //iterate over the array
//     let right = result.length - 1;

//     for (let i = 0; i < result.length; i++){
//     //check if flag is truthy
//         if (flag){
//          //reassign the left pointer node next prop to be last element in the array
//          result[left].next = result[right];
//         //increment left pointer
//         left++;
//         //decrement right pointer
//         right--;
//         //change flag to false
//         flag = false;
//         } else {
//     //otherwise, assign current (at left) next to be the current left value element in array

//         //increment left 
//         }
//     }

// //return the head
    
// };

//soln1

var reorderList = function (head) {
    let stack = [], node = head
    if (!node) return
    while (node) {
      stack.push(node)
      node = node.next
    }
  
    let len = stack.length
    node = head
    for (let i = 0; i < len; i++) {
      if (i % 2 === 0)
        node.next = stack.shift()
      else
        node.next = stack.pop()
      node = node.next
    }
    node.next = null
  };
console.log(reorderList([1,2,3,4]))

//soln2

// var reorderList2 = function(head) {
//     // find middle
// 	// by moving "fast" twice, we'll have "slow" in the middle
//     let slow = head
//     let fast = head
//     while (fast.next && fast.next.next) {
//         slow = slow.next
//         fast = fast.next.next
//     }

//     // reverse second half
// 	// with reverse linked list solution
//     let prev = null
//     let cur = slow.next
//     while (cur) {
//         let temp = cur.next
//         cur.next = prev
//         prev = cur
//         cur = temp
//     }

//     slow.next = null

//     // combine two halves
//     let h1 = head
//     let h2 = prev

//     // if even, second half will be smaller
// 	while (h2) {
//         let temp = h1.next
//         h1.next = h2
//         h1 = h2
//         h2 = temp
//     }
// };

// //neetcode

// var reorderList = function(head) {
//     const mid = getMid(head);           /* Time O(N) */
//     const reveredFromMid = reverse(mid);/* Time O(N) */

//     reorder(head, reveredFromMid);      /* Time O(N) */
// };

// const getMid = (head) => {
//     let [ slow, fast ] = [ head, head ];

//     while (fast && fast.next) {         /* Time O(N) */
//         slow = slow.next;
//         fast = fast.next.next;
//     }

//     return slow;
// }

// const reverse = (head) => {
//     let [ prev, curr, next ] = [ null, head, null ];

//     while (curr) {                      /* Time O(N) */
//         next = curr.next;
//         curr.next = prev;

//         prev = curr;
//         curr = next;
//     }

//     return prev;
// }

// const reorder = (l1, l2) => {
//     let [ first, next, second ] = [ l1, null, l2 ];

//     while (second.next) {              /* Time O(N) */
//         next = first.next;
//         first.next = second;
//         first = next;

//         next = second.next;
//         second.next = first;
//         second = next;
//     }
// }