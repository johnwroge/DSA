/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

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
 * @param {number} n
 * @return {ListNode}
 */

//andy g

var removeNthfromEnd = function (head, n) {
    let dummyHead = new ListNode(-1);
    dummyHead.next = head;
    let resultHead = dummyHead;
    let counter = 0;
    let tail = head;
    while (counter < n){
        count++;
        tail = tail.next;
    }
    let removedNode = head;
    prev = dummyHead;
    //increment our tail all the way to null
    while (tail){
        tail = tail.next;
        removedNode = removedNode.next;
        prev = prev.next;
    }
    prev.next  = removedNode.next;
    return resultHead.next; 
}



 var removeNthFromEnd = function(head, n) {
    //initialize empty array to store values
    let arr = []
    //creating a dummy node
    let res = new ListNode()
    //copy dummy node in another variable 
    let copy = res;
    //iterate over the linked list
    while(head){
        //push the current value into the array
        arr.push(head.val)
        //reassign the head to be head.next
        head = head.next;
    }
    //[1,2,3,4,5], n = 2
    //iterate over the array
    for(let i =0; i<arr.length;i++){
        //check if the array length minus i equals n, if so continue
        if(arr.length-i == n) continue;
        //reassign copy .next to be a new list node with the current element 
        copy.next = new ListNode(arr[i])
        //reassign copy to be copy.next
        copy = copy.next;
    }
    //return res.next
    return res.next;
};

//soln2 

var removeNthFromEnd = function(head, n) {
    const sentinel = new ListNode();

    sentinel.next = head;

    const fast = moveFast(sentinel, n);   /* Time O(N) */
    const slow = moveSlow(sentinel, fast);/* Time O(N) */

    slow.next = slow.next.next || null;

    return sentinel.next;
};

const moveFast = (fast, n) => {
    for (let i = 1; i <= (n + 1); i++) {/* Time O(N) */
        fast = fast.next;
    }

    return fast;
}

const moveSlow = (slow, fast) => {
    while (fast) {                     /* Time O(N) */
        slow = slow.next;
        fast = fast.next;
    }

    return slow;
}

/**
 * https://leetcode.com/problems/merge-two-sorted-lists/
 * Time O(N) | Space O(1)
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
 var removeNthFromEnd = function(head, n) {
    const length = getNthFromEnd(head, n);/* Time O(N) */

    const isHead = length < 0;
    if (isHead) return head.next;

    const curr = moveNode(head, length);  /* Time O(N) */

    curr.next = curr.next.next;

    return head
};

const getNthFromEnd = (curr, n, length = 0) => {
    while (curr) {                       /* Time O(N) */
        curr = curr.next;
        length++;
    }

    return (length - n) - 1;
}

const moveNode = (curr, length) => {
    while (length) {                    /* Time O(N) */
        curr = curr.next;
        length--;
    }

    return curr;
}

