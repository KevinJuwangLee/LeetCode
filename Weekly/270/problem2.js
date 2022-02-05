/**
 * @param {number[][]} pairs
 * @return {number[][]}
 */
var validArrangement = function(pairs) {
    let pears = {};
    let i = 0, len = pairs.length;
    while(i < len){
        let arr = pairs[i].sort(function(a, b){return a - b});
        pears[arr] = pairs[i][0] + pairs[i][1]}
        i++;
    }
    let sortedPears = Object.entries(sum).sort(([, a], [, b]) => a - b);
    console.log(sortedPears)
};