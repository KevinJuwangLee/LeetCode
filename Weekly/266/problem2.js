/**
 * @param {string} word
 * @return {number}
 */
 let vowelsList = ['a', 'e', 'i', 'o', 'u'];
 var countVowels = function(word) {
     let subs = [word[0]]
     let totalCount = 0;
     for (let i = 1; i < word.length - 1; i++) {
         subs.push(subs[i - 1] + n - 2*i)
     }
     for (let s = 1; s < word.length; s++){
        totalCount += vowelsList.indexOf(word[s]) != -1 ? subs[s] : 0;
     }
     return totalCount;
 };
