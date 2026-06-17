class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        let k = s1.length //this is going to be the length of out window
        let f1 = {};
        let f2 = {}

        // prestoring the frequency of s1
        generateFrequencyMap(s1,f1)
        generateFrequencyMap(s2.slice(0, k),f2)
        console.log("MAPS", {f1,f2})
        let left = 0;
        let right = k - 1;


        while (left <= right && right < s2.length) {
            // check of frequencies are equal, if not then shrink or expand
            let found = true
            for (let char in f1) {
                if( f1[char] !== f2[char] ){
                    found = false;
                }
            }
            if(!found) {
                console.log("1: ", left, s2[left], f2[s2[left]], f2)
                f2[s2[left]]--;
                left++;
                console.log("2: ", left, s2[left], f2[s2[left]], f2)
                
                
                console.log("3: ", right, s2[right], f2[s2[right]], f2)
                right++;
                f2[s2[right]] = 1;
                console.log("4: ", right, s2[right], f2[s2[right]], f2)
            }
            else {
                return true
            }
        }
        return false
    }
}

function generateFrequencyMap(str, obj) {
    for(let i = 0; i < str.length; i++){
            if(!obj[str[i]]) {
                obj[str[i]] = 1
            } else {
                obj[str[i]]++
            }
        }
}

