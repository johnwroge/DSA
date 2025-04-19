

function stringMatching(words: string[]): string[] {
    const w: string = words.join(' ');
    const count = (str: string, searchStr: string): number => str.split(searchStr).length - 1;
    let result: string[] = [];
    for (let word of words){
        if (count(w, word) > 1){
            result.push(word)
        }
    }
    return result; 
};