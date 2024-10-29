

function alienOrder(words){
    const adj = new Map();
    for (let i = 0; i < words.length; i++){
        for (let char of words[i]){
            adj.set(char, new Set())
        }
    }
    let queue = new Queue(); 
    console.log(queue)

    for (let i = 0; i < words.length; i++){
        let [w1, w2] = [words[i], words[i + 1]]
        let minLen = Math.min(w1.length,w2.length);
       
    }
}

const words = ['wrt','wrf','er','ett','rftt']
console.log(alienOrder(words))