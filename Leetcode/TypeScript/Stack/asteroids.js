/*
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction
 (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode. Two asteroids
 moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
*/

// var asteroidCollision = function(asteroids) {
 
//     const stack = [];

//     for (let i = 0; i < asteroids.length; i++){
//         if (asteroids[i] > 0 && asteroids[i + 1] < 0){
//           if (Math.abs(asteroids[i]) > Math.abs(asteroids[i + 1])){
//             stack.push(asteroids[i])
//           } else {
//             stack.pop();
//           }
//         }   
//         else {
//             stack.push(asteroids[i]);
//         }
//     }

// return stack;
// };

const asteroidCollision = (asteroids) => {
    //create a stack 
    let stack = [];

    //iterate over the asteroids array 
    for (asteroid of asteroids) {
        //loop while the stack length is not 0 and the asteroid is not less than 0 and 
        //stack.at(-1) is shorthand for last element in the array
        while (stack.length != 0 && asteroid < 0 && stack.at(-1) > 0) {
            //calculate difference -> positive or negative
            let diff = asteroid + stack.at(-1);

            //if negative asteroid is larger
            if (diff < 0) {
                stack.pop();
                //otherwise if positive asteroid is larger
            } else if (diff > 0) {
                asteroid = 0;
            } else {
                asteroid = 0;
                stack.pop();
            }
        }
        
        if (asteroid) {
            stack.push(asteroid);
        }
    }
    return stack;
};


//console.log(asteroidCollision([-2,-1,1,2]))
// console.log(asteroidCollision([-2,-2,1,-2]))
console.log(asteroidCollision([5,10,-5]))
// console.log(asteroidCollision([-2,-1,1,2]))