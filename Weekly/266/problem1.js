/**
 * @param {string} word
 * @return {number}
 */

 let vowelsList = ['a', 'e', 'i', 'o', 'u'];
 var countVowelSubstrings = function(word) {
    let count = 0;
    for(let i = 0; i < word.length - 1; i++){
        let vowels = {'a': 0, 'e': 0, 'i': 0, 'o':0, 'u':0};
        if(vowelsList.indexOf(word[i]) === -1){
            continue;
        }
        vowels[word[i]] = true;
        for(let j = i + 1; j < word.length; j++){
            if(vowelsList.indexOf(word[j]) != -1){
                vowels[word[j]] += 1;
                if(check(vowels)){
                    count++;
                }
            } else{break}
        }
        
    }
    return count;
};


function check(vowels){
    let successful = true;
        for(let vowel in vowels){
            if(vowels[vowel] === 0){
                successful = false;
                break;
            }
        }
        if(successful){
            return true;
        }
}

