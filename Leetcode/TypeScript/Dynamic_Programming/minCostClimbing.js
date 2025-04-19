



var minCostClimbingStairs = function(cost) {
let minone = cost[0];
let mintwo = cost[1];

for (let i = 2; i < cost.length; i++){
    let curr = cost[i] + Math.min(minone, mintwo);
    minone = mintwo;
    mintwo = curr;
}
return Math.min(minone, mintwo)  
};

console.log(minCostClimbingStairs([0,1,1,0,3,7,5,3,2,7,10,0,1,2,0,3,7,5,8,0,1,0,2,0,55,3,1]))