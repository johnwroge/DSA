/*

Given an array of integers, sort the array in-place and return the array.
Do not create a new array in memory. Instead, modify the array as given. Do not
use the array sort method built in to the array prototype while solving the
problem. The integers should be in ascending order from left to right.

We will sort the array using a strategy called selection sort, which works as
follows. First, put the smallest number in the array at position 0. Then, put
the second-smallest number in the array at position 1. Then, put the
third-smallest number in the array at position 2 etc. After going through the
whole array, the array will end up being sorted.

*/

// const swap = (arr, i, j) => {
//    return [arr[i], arr[j]] = [arr[j], arr[i]];
// }

const selectionSort = array => {
    if (!array.length) return array; 
    let min;
    for (let i = 0; i < array.length; i++){
       min = i;
       for (let j = i + 1; j < array.length; j++){
        if (array[j] < array[min]){
            min = j;
        }
       }
       if (min != i){
        [array[min], array[i]] = [array[i], array[min]]
       }
}
  return array; 
};


function selectionSort2 (array){

//iterate from i = 0 to end of array
for (let i = 0; i < array.length; i++){
//initialize index to be i
let index = i; 
for (let j = i; j < array.length; j++){
//iterate from j = i to end of arr
  if (array[j] < array[index]){
  //check if array[j] < array[i]
    //reassign index to be j
    index = j;
  }

}
   //reassign ith array element to be the current index (the lowest value)
   [array[i], array[index]] = [array[index], array[i]]

}
//return the sorted the array
return array; 

}

console.log(selectionSort2([4,7,4,9,11,3]))









//console.log(selectionSort([4,2,7,8,3,5,11,8,33,0,33,2]))
/*

Extension:

Given an array of integers, sort the array in-place and return the array.
Do not create a new array in memory. Instead, modify the array as given. Do not
use the array sort method built in to the array prototype while solving the
problem. The integers should be in ascending order from left to right.

For this extension, we will use a strategy called insertion sort, which works as
follows. Imagine that the first k - 1 numbers of the array are in ascending
order. We take the kth number and insert it into the correct position amongst
the k - 1 numbers such that now, the first k numbers of the array are in
ascending order. In other words:

The first value in the array is considered to be already fine.
The second value is either placed before/after the first value.
The third value is inserted in the correct position amongst the first two values.
The fourth value is inserted in the correct position amongst the first three values.
etc.

*/

const insertionSort = arr => {
    for (let i = 1; i < arr.length; i++){
        let currentVal = arr[i];
        for (var j = i - 1; j >= 0 && arr[j] > currentVal; j--){
          arr[j + 1] = arr[j];
        }
        arr[j + 1] = currentVal; 
      }
      return arr;
};

module.exports = {selectionSort, insertionSort};
