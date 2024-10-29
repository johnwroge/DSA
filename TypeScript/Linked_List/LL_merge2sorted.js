/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
*/

var mergeTwoLists = function(list1, list2) {
    //create dummy variable assigned to new node with -infinity
        // (should be smallest as it's first)
    let dummy = new ListNode(-Infinity);
    //create a prev value and assign to this dummy node
    let prev = dummy; 
    //loop while l1 and l2 are truthy
    while (l1 && l2){
        //check if l1 val is less than or equal to l2 val
        if (l1.val <= l2.val){
            //assign prev.next to be l1
            prev.next = l1;
            //reassign prev to be l1
            prev = l1;
            //reassign l1 to be l1.next
            l1 = l1.next;
        } else {
        //otherwise
            //assign prev.next to be l2
            prev.next = l2;
            //reassign prev to be l2
            prev = l2; 
            //reassign l2 to be l2.next
            l2 = l2.next;
        }
    }
    //(edge case: in case l1 and l2 are unequal in size)
    //check if not l1, assign prev/next to be l2
    if (!l1) prev.next = l2;
    //check if not l2, assign prev.next to be l1
    if (!l2) prev.next = l1;

    return dummy.next; 
};