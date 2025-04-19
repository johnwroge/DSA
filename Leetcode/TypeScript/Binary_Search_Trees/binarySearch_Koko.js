/*
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
 and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
 and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
*/

//brute force: 
/**
 * Time O(N * log(M)) | Space O(1)
 * 
 */
 var minEatingSpeed = function (piles, h) {
    //assign left and right pointers to be 1 and maximum of piles (respectively)
    let [left, right] = [1, Math.max(...piles)];
    //loop while left is less than right
    while (left < right) {
        //calculate mid variable 
        const mid = (left + right) >> 1;
        //get the hour spent with mid and piles
        const hourSpent = getHourSpent(mid, piles);

        //store conditional in variable if target is greater
        const isTargetGreater = h < hourSpent;
        if (isTargetGreater) left = mid + 1;
        //
        const isTargetLess = hourSpent <= h;
        if (isTargetLess) right = mid;
    }

    return right;
};

const getHourSpent = (mid, piles, hourSpent = 0) => {
    for (const pile of piles) {
        hourSpent += Math.ceil(pile / mid);
    }

    return hourSpent;
};
console.log(minEatingSpeed([3,6,7,11], 8))