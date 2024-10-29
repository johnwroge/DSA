/* 

Given a string that represents a Binary Number, write a function that converts this string into a decimal number. DO NOT use the native parseInt() method. 

For example: 

binToDec('0')   -> 0
binToDec('11')  -> 3
binToDec('100') -> 4
binToDec('101') -> 5
binToDec('0101') -> 5

For more information on how to read binary, check out this article: 
https://m.wikihow.com/Read-Binary

*/

function binToDec(binString){
//create output variable
let result = 0;
let j = 0;
    //iterate over string characters from right to left for 6 spaces starting at index 0
    for (let i = binString.length - 1; i >= 0; i--){
        
        if(binString[i] === undefined || binString[i] === 0){
            result += 0;
        } else {
        result += binString[i] * Math.pow(2,j);
        }
        //add result to output;
        j++;
    }

//return output;
return result; 

}

console.log(binToDec('0'))  //-> 0
console.log(binToDec('11'))  //-> 3
console.log(binToDec('100')) //-> 4
console.log(binToDec('101')) //-> 5
console.log(binToDec('0101')) //-> 5

module.exports = {binToDec};

function busSchedule(arr, timeGiven) {
    let timenow = parseInt(timeGiven.substring(0,2)) * 60
    let res = 0
    arr.sort((a,b) => a -  b)
    let time = []
    for (let s of arr){
        let val = parseInt(s.substring(0,2)) * 60 + parseInt(s.substring(3))
        time.push(val)
    }

    for (let i = time.length - 1; i > 0; i--){
        if (timenow > time[i]){
            return timenow - time[i]
        }
    }


}