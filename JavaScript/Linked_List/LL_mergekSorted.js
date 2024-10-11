/*
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

const mergeKLists = function(lists) {
    const queue = new MinPriorityQueue({ priority: x => x.val })
  
    for (const head of lists) {
      if (head) {
        queue.enqueue(head)
      }
    }
  
    let result = new ListNode()
    const head = result
  
    while (!queue.isEmpty()) {
      const { val, next } = queue.dequeue().element
  
      result.next = new ListNode(val)
      result = result.next
  
      if (next) {
        queue.enqueue(next)
      }
    }
  
    return head.next
  }

//   neetcode

/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * Time O(N) | Space O(N)
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
 var mergeKLists = function(lists) {
    let previous = null;

    for (let i = 0; i < lists.length; i++) {
        previous = mergeTwoLists(previous, lists[i]);
    }

    return previous;
};

var mergeTwoLists = function(list1, list2) {
    let sentinel = tail = new ListNode(0);

    while (list1 && list2) {
        const canAddL1 = list1.val <= list2.val;
        if (canAddL1) {
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }

        tail = tail.next;
    }

    tail.next = list1 || list2;

    return sentinel.next;
};

/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * Time O(N * log(K)) | Space O(N + K)
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
 var mergeKLists = function(lists) {
    const minHeap = getMinHeap(lists);
    return mergeLists(minHeap)
};

const getMinHeap = (lists) => {
    const heap = new MinPriorityQueue({ priority: ({ val }) => val });
    for (const node of lists) {
        if (!node) continue;
        heap.enqueue(node);
    }
    return heap;
}


const mergeLists = (minHeap) => {
    let sentinel = tail = new ListNode();
    while (!minHeap.isEmpty()) {
        const node = minHeap.dequeue().element;
        tail.next = node;
        tail = tail.next;
        if (!node.next) continue;

        minHeap.enqueue(node.next);
    }

    return sentinel.next;
}

/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * Time O(N) | Space O(N)
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
 var mergeKLists = function(lists) {
    let previous = null;

    for (let i = 0; i < lists.length; i++) {
        previous = mergeTwoLists(previous, lists[i]);
    }

    return previous;
};

var mergeTwoLists = function(list1, list2) {
    let sentinel = tail = new ListNode(0);

    while (list1 && list2) {
        const canAddL1 = list1.val <= list2.val;
        if (canAddL1) {
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }

        tail = tail.next;
    }

    tail.next = list1 || list2;

    return sentinel.next;
};

/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * Time O(N * log(K)) | Space O(N + K)
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
 var mergeKLists = function(lists) {
    const minHeap = getMinHeap(lists);

    return mergeLists(minHeap)
};

const getMinHeap1 = (lists) => {
    const heap = new MinPriorityQueue({ priority: ({ val }) => val });

    for (const node of lists) {
        if (!node) continue;

        heap.enqueue(node);
    }

    return heap;
}


const mergeLists1 = (minHeap) => {
    let sentinel = tail = new ListNode();

    while (!minHeap.isEmpty()) {
        const node = minHeap.dequeue().element;

        tail.next = node;
        tail = tail.next;

        if (!node.next) continue;

        minHeap.enqueue(node.next);
    }

    return sentinel.next;
}



























































