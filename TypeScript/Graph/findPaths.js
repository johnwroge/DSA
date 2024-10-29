var findPaths = function(m, n, maxMove, startRow, startColumn) {
    const memo = {};
    const MOD = Math.pow(10, 9) + 7;
    const go = (i, j, count) => {
        let key = `${i}-${j}-${count}`;
        if (count < 0) {
            return 0;  // if we're out of moves, let's stop 
        }
        if (memo[key] !== undefined) { // check the memoization map
            return memo[key]; 
        }
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return 1; // if we're out of bounds, let's count it as 1
        }
        return memo[key] = (
            go(i + 1, j, count - 1) + // go south
            go(i, j + 1, count - 1) + // go east
            go(i - 1, j, count - 1) + // go north
            go(i, j - 1, count - 1)   // go west
        ) % MOD;
    }
    return go(startRow, startColumn, maxMove);
};



console.log(findPaths(2,2,2,0,0))